from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.authtoken.models import Token

# Create your views here.

def index(request):
    authenticated = True
    if not request.user.is_authenticated:
        authenticated = False
    
    content = {
        'authenticated' : authenticated
    }

    return render(request, 'index.html', content)

def signup(request):
    if request.method == 'POST':
        firstname  = request.POST['firstname']
        lastname   = request.POST['lastname']
        email      = request.POST['email']
        phone      = request.POST['phone']
        password   = request.POST['password']
        username   = request.POST['username']

        user = User.objects.create_user(username= username, email= email, password= password, is_active = True, is_staff = True)

        Profile.objects.create(user= user, firstname = firstname, lastname=lastname, email=email, phone=phone, username = username, password = password)

        token = Token.objects.create(user = user)
        print(token)
        messages.success(request, "Your response has been recorded successfully!")
                
        return redirect('index')
    return render(request, 'signup.html')

def login_view(request):
    if request.POST:
        username      = request.POST['username']
        password   = request.POST['password']
        user       = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Invalid username or password!")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "We're sorry you had to leave. We would love to see you soon!")
    return redirect('index')

@login_required(redirect_field_name='login')
def change_password(request):
    if request.method == 'POST':
        user     = request.user
        password = request.POST['password']

        if password:
            user.set_password(password)
            user.save()

            model = Profile.objects.get(user = user)
            model.password = password
            model.save()

            messages.success(request, "Your password has been successfully changed!")
            return redirect('index')
    return render(request, 'change_password.html')



# superuser
# username = admin
# password = admin123