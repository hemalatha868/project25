from django.shortcuts import render

# Create your models here.
from app.forms import *
from django.http import HttpResponse


def django_forms(request):
    formobject=Studentform()
    d={'form':formobject}

    if request.method=="POST":
        FD=Studentform(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            p=FD.cleaned_data['password']
            ad=FD.cleaned_data['address']
            g=FD.cleaned_data['gender']
            c=FD.cleaned_data['course']
            t=FD.cleaned_data['time']
            d=FD.cleaned_data['date']
            dt=FD.cleaned_data['datetime']
            d1={'n':n, 'a':a, 'e':e, 'p':p, 'ad': ad, 'g':g, 'c':c, 't':t, 'd':d, 'dt':dt}
            return render(request,'form_data.html', d1)
    return render(request,'django_forms.html',d)

