from django.shortcuts import render
from .models import Membership


def membershipOptions(request):
    member = Membership.objects.all()
    return render(request,'memberoptions.html',{'membership':member})


def membershipForm(request):
    return render(request,'membershipform.html')