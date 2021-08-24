from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import logout, login, authenticate
from django.http.response import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required
def logout_view(request):
    logout(request)
    response = redirect('/')
    response.delete_cookie('site_color_mode')
    messages.success(request, 'Logged out sucessfully. Now scram.')
    return response

def login_view(request):
    template_name = "login.html"
    form = LoginForm()
    context = {'form' : form}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Log in sucessful. Welcome Traveler.')
            response = redirect('/')
            if request.user.is_authenticated :
                response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
            elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
                response.set_cookie('site_color_mode', 'light', max_age = 5000000)
            return response
        else:
            return redirect('login')
    elif request.method == 'GET' :
        return render(request, template_name, context)

def signup_view(request):

    template_name = "signup.html"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})

def password_reset_view(request): #todo
    return HttpResponse("forgot to implement that one, mb")
