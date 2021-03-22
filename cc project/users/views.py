from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
            ## username = form.cleaned_data.get('username') ##
                messages.success(request, f'You have successfully created your account! You can login now.')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/signup.html', {'form': form, 'title':'Register'})

@login_required
def profile(request):
    data = {}
    data['firstname'] = request.user.first_name
    data['username'] = request.user.username
    data['email'] = request.user.email
    data['date_joined'] = request.user.date_joined
    data['last_name'] = request.user.last_name
    return render(request, 'users/profile.html', {'context':data, 'title':'Profile'})

def alt_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
