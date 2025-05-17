from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    # Show the home page
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('customers')  # Changed from dashboard to customers
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('login')
    else:
        # Render the signin page
        return render(request, 'signin.html')

def dashboard(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records})
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('customers')  # Changed from dashboard to customers
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('login')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('dashboard')
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('login')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('dashboard')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('login')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('dashboard')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request,"You have logged out")
    return redirect('home')

def customers(request):
    # You may want to add actual customer data here if you have any
    return render(request, 'customers.html')