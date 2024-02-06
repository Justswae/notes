from django.shortcuts import render, redirect
from . forms import SignupForm  
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 

def index(request):
    return render(request, 'templates/core/index.html')

def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)

        if signupform.is_valid():
            user = signupform.save()
            login(request, user)
            return redirect('/')
        
    signupform = SignupForm()
    return render(request, 'templates/auth/signup.html', {
        'signupform': signupform,
        
    })

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    return render(request, 'templates/user/profile.html')
