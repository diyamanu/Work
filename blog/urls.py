from django.urls import path
from .views import *
urlpatterns=[
    path("",welcome,name="Welcome"),
    path("Grade/",Garde,name="Grade"),
    path("Hour/",Hour,name="Hour"),
    path("Sub1/", Sub1, name="Sub1"),
    path("Sub/", Sub, name="Sub"),
]