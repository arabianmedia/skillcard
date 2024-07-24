from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('apply/', views.apply, name="apply"),
    path('cards/', views.allcards, name="cards"),
    path('apply/<slug:slug>', views.applyform, name="applyform"),
    path('card/<slug:slug>', views.CardDetails, name="cardDetails"),

]



