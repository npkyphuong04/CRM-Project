from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.db import connections
import json
from django.http import JsonResponse
from django.db.models import Count
import os
from django.conf import settings
import pandas as pd


def home(request):
    records = Record.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")

    return redirect('home')


def dashboard(request):
    if not request.user.is_authenticated:
        messages.success(request, "You Must Be Logged In To View The Dashboard...")
        return redirect('home')

    # Load the CSV data
    csv_path = os.path.join(settings.BASE_DIR, 'CRM_Application', 'static', 'data', 'clean_data.csv')
    df = pd.read_csv(csv_path)

    # Get unique events and regions for filters
    all_events = sorted(df['EventName'].unique())
    all_regions = sorted(df['Region'].unique())

    # Handle filter parameters from request
    selected_events = request.GET.getlist('events')
    selected_regions = request.GET.getlist('regions')

    # Set default selection to 'purchase' if no events selected
    if not selected_events:
        if 'purchase' in all_events:
            selected_events = ['purchase']
        else:
            selected_events = all_events

    # Set default selection to 'Ho Chi Minh City' if no regions selected
    if not selected_regions:
        if 'Ho Chi Minh City' in all_regions:
            selected_regions = ['Ho Chi Minh City']
        else:
            selected_regions = all_regions

    # Filter data based on selections
    filtered_data = df[
        (df['EventName'].isin(selected_events)) &
        (df['Region'].isin(selected_regions))
        ]

    # Calculate total events (total row count after filtering)
    total_events = len(filtered_data)

    # Calculate total sessions (unique SessionID count after filtering)
    total_sessions = len(filtered_data['SessionID'].unique())

    # Count events and regions for dropdown labels
    event_counts = df['EventName'].value_counts().to_dict()
    region_counts = df['Region'].value_counts().to_dict()

    # Initialize empty data structures for the charts
    top_items_data = {'labels': [], 'values': []}
    top_sources_data = {'labels': [], 'values': []}

    # Only process item data if we have filtered data
    if not filtered_data.empty:
        # Generate top 10 items data (excluding empty or special values)
        items_to_exclude = ['<unset>', '', '(not set)', None]
        items_data = filtered_data[~filtered_data['ItemName'].isin(items_to_exclude)]

        if not items_data.empty:
            # Ensure ItemName column exists and has valid data
            if 'ItemName' in items_data.columns and not items_data['ItemName'].isna().all():
                # Limit to top 10 to avoid performance issues
                top_items = items_data['ItemName'].value_counts().nlargest(10)
                top_items_data = {
                    'labels': top_items.index.tolist(),
                    'values': top_items.values.tolist()
                }

        # Generate top 10 sources data
        if 'Source' in filtered_data.columns and not filtered_data['Source'].isna().all():
            sources_data = filtered_data[filtered_data['Source'].notna()]
            if not sources_data.empty:
                # Limit to top 10 to avoid performance issues
                top_sources = sources_data['Source'].value_counts().nlargest(10)
                top_sources_data = {
                    'labels': top_sources.index.tolist(),
                    'values': top_sources.values.tolist()
                }

    # Create context with safe default values
    context = {
        'events': all_events,
        'regions': all_regions,
        'selected_events': selected_events,
        'selected_regions': selected_regions,
        'total_events': total_events,
        'total_sessions': total_sessions,  # Corrected calculation
        'event_counts': json.dumps(event_counts),
        'region_counts': json.dumps(region_counts),
        'top_items_data': json.dumps(top_items_data),
        'top_sources_data': json.dumps(top_sources_data),
    }

    return render(request, 'dashboard.html', context)