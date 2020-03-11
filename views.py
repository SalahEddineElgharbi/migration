from django.shortcuts import render 
from . makk import ppost

def inde(request):
    posts = ppost.objects.all()
    return render(request, 'blogg/index.html',{'posts':posts})
    # comme ona 2 index.html donc blogg jeuer role de name space 

def show(request,id):
	post= ppost.objects.get(id=id)
	return render(request,'blogg/show.html',{'post':post})

def  handler404(request):
    return render(request,' errors/404.html',status=404)	