from django.urls import path
from .views import *
urlpatterns = [
    path('', welcome),
    path('index', index),
    path('listclass', listclass),
    path('addclass', addclass),
    path('deleteclass', deleteclass),
    path('success', success, name = 'success')
]
