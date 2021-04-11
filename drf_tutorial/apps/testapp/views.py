from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("hello world")


def hello2(request):
    data = {'data2':'hello world!'}
    return render(request,'test.html',data)

def hello3(request):
    return JsonResponse({'num':129})