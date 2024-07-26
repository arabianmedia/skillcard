from django.urls import path
from . import views

urlpatterns = [

    path('', views.membershipOptions, name="membershipOptions"),
    path('apply/', views.membershipForm, name="membershipForm"),

]




