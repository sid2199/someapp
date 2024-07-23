'''
    ChatRoom Home Page
'''
from django.shortcuts import render


CONTEXT = {}


def index(request):
    '''
        render index.html, the chatroom home page
    '''
    context = {}
    return render(request, "chatroom/index.html", context)
