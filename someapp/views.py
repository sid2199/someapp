'''
    Home Page
'''
from django.shortcuts import render


def index(request):
    '''
        render index.html, the home page
    '''
    context = {}
    return render(request, "someapp/index.html", context)
