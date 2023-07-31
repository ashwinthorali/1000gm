from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm, LoginForm
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect 



def login_user(request):
    
    if request.method == "POST":
        # your sign in logic goes here
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #authenticate checks if credentials exists in db
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login In Successful')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

                else:
                    return HttpResponse("Wait till verification")
                    
            else:
                return HttpResponse("Invalid login")
    return render(request, 'index.html')


def singup(request):
    
    user_form = RegisterForm()
    profile_form = ProfileForm()
    form = LoginForm()
    if request.method == "POST":
        print("here 3")
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile =  profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print('HEllo')
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        else:
            messages.error(request, 'Please correct the error below.')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
  

def byebye(request):
    logout(request)
    messages.success(request, 'Logout In Successful')
    return redirect ('home:home')