from django.urls import path

from chatroom.views import index

urlpatterns = [
    path('', index),
]