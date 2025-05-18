from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('customers')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('customers')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def customer_record(request, pk):
    customer_record = get_object_or_404(Record, id=pk)
    return render(request, 'record.html', {'customer_record': customer_record})


@login_required(login_url='login')
def delete_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    messages.success(request, "Record deleted successfully.")
    return redirect('customers')  # hoặc 'dashboard' nếu bạn có


@login_required(login_url='login')
def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully.")
            return redirect('customers')
    else:
        form = AddRecordForm()
    return render(request, 'add_record.html', {'form': form})


@login_required(login_url='login')
def update_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully.")
            return redirect('customers')
    else:
        form = AddRecordForm(instance=record)
    return render(request, 'update_record.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('home')


@login_required(login_url='login')
def customers(request):
    # Nếu có dữ liệu khách hàng thì truyền vào context ở đây
    return render(request, 'customers.html')
