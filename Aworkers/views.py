from django.shortcuts import render
from django.urls  import path



def  workers(request):
    context = {'yossi':'yossi'}
    return render(request,'Aworkers/worker.html',context)
def  workers1(request,pk):
    context = {'pk':pk}
    return render(request,'Aworkers/worker1.html',context)