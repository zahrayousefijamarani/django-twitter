from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from loan.models import Customer


def loan(request):
    return render(request, './loan/loan.html', context={})


def signup(request):
    return render(request, './loan/signUp.html', context={})


def passmale(optionalRadio):
    if optionalRadio == 'option1':
        return True;
    return False


def submit(request):
    name = request.POST['name']
    lastname = request.POST['lastname']
    fathername = request.POST['fathername']
    nationalId = request.POST['nationalId']
    id = request.POST['Id']
    birthday = request.POST['birthday']
    phoneNumber = request.POST['phoneNumber']
    password = request.POST['password']
    optionalRadio = request.POST['optionsRadios']
    region = request.POST['region']
    try:
        c = Customer(name=name, lastName=lastname, fatherName=fathername
                     , nationalId=nationalId, birthday=birthday, phoneNumber=phoneNumber,
                     password=password, male=passmale(optionalRadio), region=region)

        c.save()
    except:
        raise Http404("sth is wrong !")
    return HttpResponseRedirect(reverse('loan:homepage', args=(c.nationalId,)))


def homepage(request, id):
    return render(request, './loan/homepage.html', context={
        'Id': id
    })
