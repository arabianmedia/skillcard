from django.shortcuts import render,get_object_or_404
from certificate.models import Application


def verify(request):

    if request.method == "POST":
        regno = request.POST['regno']

        try:
            usr = Application.objects.get(registration_no=regno)
        except:
            usr = "No Users Found !!!!"

        return render(request,"verifycard.html",{'usr':usr})
    
    return render(request,"verifycard.html")