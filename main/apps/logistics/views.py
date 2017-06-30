from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):


    return render(request, 'logistics/index.html')
