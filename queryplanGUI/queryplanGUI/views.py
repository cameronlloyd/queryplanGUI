from django.http import HttpResponse
from django.shortcuts import render
import os
def index(request):
    context = {}
    return render(request, 'queryplanGUI/index.html', context)

