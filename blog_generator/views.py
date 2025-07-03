from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']

        if password != repeat_password:
            error_message = "Password do not match"
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except Exception as e:
                error_message = f"Error creating account: {e}"
                return render(request, 'signup.html', {'error_message': error_message})
    return render(request, 'signup.html')

def user_logout(request):
    return render(request, 'logout.html')
