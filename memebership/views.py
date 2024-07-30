from django.shortcuts import render
from .models import Membership,MembershipApplication
from datetime import datetime

def membershipOptions(request):
    member = Membership.objects.all()
    return render(request,'memberoptions.html',{'membership':member})



def membershipForm(request):

    if request.method == 'POST':
        company_name = request.POST['companyName']
        asbestos_removal = request.POST['asbestosRemoval']
        contact_name = request.POST['contactName']
        address = request.POST['address']
        postcode = request.POST['postcode']
        telephone = request.POST['telephone']
        email = request.POST['email']
        website = request.POST['website']

        training_contact_name = request.POST['trainingContactName']
        training_contact_email = request.POST['trainingContactEmail']

        audit_contact_name = request.POST['auditContactName']
        audit_contact_email = request.POST['auditContactEmail']

        marketing_contact_name = request.POST['marketingContactName']
        marketing_contact_email = request.POST['marketingContactEmail']

        regional_contact_name = request.POST['regionalContactName']
        regional_contact_email = request.POST['regionalContactEmail']

        accounts_contact_name = request.POST['accountsContactName']
        accounts_contact_email = request.POST['accountsContactEmail']

        additional_telephone = request.POST['additionalTelephone']
        additional_postcode = request.POST['additionalPostcode']
        company_reg_no = request.POST['companyRegNo']
        vat_reg_no = request.POST['vatRegNo']

        signature = request.POST['signature']
        position = request.POST['position']

        # Convert date format from DD/MM/YYYY to YYYY-MM-DD
        date_str = request.POST['date']
        date = datetime.strptime(date_str, '%d/%m/%Y').date()

        health_safety_statement = request.FILES['healthSafetyStatement']
        liability_insurance = request.FILES['liabilityInsurance']
        company_registration = request.FILES['companyRegistration']

        application = MembershipApplication(
            company_name=company_name,
            asbestos_removal=asbestos_removal,
            contact_name=contact_name,
            address=address,
            postcode=postcode,
            telephone=telephone,
            email=email,
            website=website,
            training_contact_name=training_contact_name,
            training_contact_email=training_contact_email,
            audit_contact_name=audit_contact_name,
            audit_contact_email=audit_contact_email,
            marketing_contact_name=marketing_contact_name,
            marketing_contact_email=marketing_contact_email,
            regional_contact_name=regional_contact_name,
            regional_contact_email=regional_contact_email,
            accounts_contact_name=accounts_contact_name,
            accounts_contact_email=accounts_contact_email,
            additional_telephone=additional_telephone,
            additional_postcode=additional_postcode,
            company_reg_no=company_reg_no,
            vat_reg_no=vat_reg_no,
            signature=signature,
            position=position,
            date=date,
            health_safety_statement=health_safety_statement,
            liability_insurance=liability_insurance,
            company_registration=company_registration
        )
        application.save()

        return render(request,'thankyou.html',{'tmessage':'Successfully Applied for Member','regno':"You Need for wait for 24 hour afer verifying your details your account is successfully verified!!" })

    return render(request,'membershipform.html')





def memebers(request):
    memberss = MembershipApplication.objects.all()
    return render(request,'allmember.html',{'members':memberss})