from django.shortcuts import render,HttpResponse,redirect
from connections.models import Contact
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from connections.models import Circle,Division,SubDivision,Consumer

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        issue = request.POST.get('issue')
        contact = Contact (name = name, email = email, phone = phone, issue = issue)
        contact.save()
        messages.success(request, "Your complaint/query has been sent!")
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is already in used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Name is already in used.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully!!!")
                return redirect('register')
        else:
            messages.info(request, "Passwords do not match.")
            return redirect('register')
    else:
        #method="GET"  
        return render(request, 'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user has entered correct credentials
        user = auth.authenticate(username=username, password=password)

        if user is not None:
    # A backend authenticated the credentials
            auth.login(request,user)
            messages.success(request,"User logged in successfully!")
            return redirect("index")
        else:
    # No backend authenticated the credentials
            messages.info(request,"User not found! Please enter correct credentials")
            return render(request,'login.html')
    else:
        return render(request, 'login.html')
    
def userlogout(request):
   auth.logout(request)
   return redirect ("/login")

def connection(request):
    return render(request, 'connection.html')
    
def person_create_view(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_responses')  # Redirect to the view_responses page
    else:  # If the request method is GET
        form = PersonCreationForm()

    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Consumer, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})

def confirm(request):
    success_message = messages.get_messages(request)
    return render(request, 'confirm.html', {'success_message': success_message})

def view_form(request):
    if request.method == 'POST':
        form_data = request.POST  # Assuming you want to show the submitted data on the same page
        return render(request, 'view_form.html', {'form_data': form_data})
    else:
        return render(request, 'form.html')

def view_responses(request):
    #name = request.POST.get('name')
    if request.method == 'POST':
        name = request.POST.get('name')
        form_responses = Consumer.objects.filter(name=name)         # Retrieve form responses from the database
        #form_responses = Consumer.objects.all()                    # Retrieve all form responses from the database
        return render(request, 'view_responses.html', {'form_responses': form_responses})
    else:
        return render(request, 'form.html')

# AJAX
def load_division(request):
    circle_id = request.GET.get('circle_id')
    divisions = Division.objects.filter(circle_id=circle_id).all()
    return render(request, 'division_dropdown_list_options.html', {'divisions': divisions})

def load_subdivision(request):
    division_id = request.GET.get('division_id')
    subdivisions = SubDivision.objects.filter(division_id=division_id).all()
    return render(request, 'subdivision_dropdown_list_options.html', {'subdivisions': subdivisions})
    # return JsonResponse(list(divisions.values('id', 'name')), safe=False)