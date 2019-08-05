from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from awesomeTwitter.models import Person, Message


@login_required
def main_page(request):
    return render(request, './awesomeTwitter/main.html', context={
        'users': Person.objects.all()
    })


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    if username and password:
        user = authenticate(username=username, password=password)
        if not username:
            return HttpResponse('Incorrect username')
        if not user.check_password(password):
            return HttpResponse('Incorrect password')
        if not user.is_active:
            return HttpResponse('It is not active')
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('twitter:main', args=(())))
    else:
        return HttpResponseRedirect(reverse('login', args=(())))


def login_func(request):
    return render(request, './awesomeTwitter/login.html', context={})


def createUser(request):
    try:
        userName = request.POST['username']
        userPass = request.POST['password']
        user = User.objects.create(username=userName, password=userPass)
        user.save()
        new_user = authenticate(username=userName, password=userPass)
        login(request, new_user)
        return HttpResponseRedirect(reverse('twitter:main', args=()))
    except:
        return HttpResponseRedirect(reverse('signup', args=(())))


def sign_up(request):
    return render(request, './awesomeTwitter/signup.html', context={})


@login_required
def go_profile(request, Id):
    user = Person.objects.get(id=Id)
    return render(request, './awesomeTwitter/profile.html', context={
        'Id': Id,
        'user': user,
        'messages': user.message_set.all()
    })


@login_required
def messaging(request, Id):
    person = Person.objects.get(pk=Id)
    m = person.message_set.create(text=request.POST['msg'])
    return render(request, './awesomeTwitter/profile.html', context={
        'Id': Id,
        'user': person,
        'messages': person.message_set.all()
    })


@login_required
def deleting(request, pId, mId):
    person = Person.objects.get(pk=pId)
    m = person.message_set.get(pk=mId)
    m.delete()
    return render(request, './awesomeTwitter/profile.html', context={
        'Id': pId,
        'user': person,
        'messages': person.message_set.all()
    })

# def login_requested(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data('username')
#             password = form.cleaned_data('password')
#             user = authenticate(username, password)
#             if user in None:
#                 login(request, user)
#                 messages.info(request, "logged in")
#     form = AuthenticationForm()
