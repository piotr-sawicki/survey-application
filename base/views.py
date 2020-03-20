from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_first_view(request):
    return HttpResponse('hello world')
    # render(request, , {})