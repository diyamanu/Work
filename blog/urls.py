from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('listclass', listclass),
    path('addclass', addclass),
]
