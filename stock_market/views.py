from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Data


def say_hello(request):
    return HttpResponse("Hello From Janata Wifi")

def index(request):
    
    mem=Data.objects.all()
    return render(request, 'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['date']
    y=request.POST['trade_code']
    z=request.POST['high']
    a=request.POST['low']
    b=request.POST['open']
    c=request.POST['close']
    d=request.POST['volume']
    mem=Data(date=x,trade_code=y,high=z,low=a,open=b,close=c,volume=d)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Data.objects.get(id=id)
    mem.delete()
    return redirect("/")

def upadte(request,id):
    mem=Data.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})


def uprec(request,id):
    x=request.POST['date']
    y=request.POST['trade_code']
    z=request.POST['high']
    a=request.POST['low']
    b=request.POST['open']
    c=request.POST['close']
    d=request.POST['volume']
    mem=Data.objects.get(id=id)
    mem.date=x
    mem.trade_code=y
    mem.high=z
    mem.low=a
    mem.open=b
    mem.close=c
    mem.volume=d
    mem.save()
    return redirect("/")
