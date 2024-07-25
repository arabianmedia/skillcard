from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import cardDetails,Application
from django.contrib import messages
from django.utils.text import slugify
import uuid
from datetime import datetime
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    card = cardDetails.objects.all()
    return render(request,'index.html',{'cards' : card})



def apply(request):
    card = cardDetails.objects.all()
    return render(request,'apply.html',{'cards' : card})



def applyform(request,slug):
    card = get_object_or_404(cardDetails, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        ni_number = request.POST.get('ni_number')
        town_city = request.POST.get('town_city')
        dob = request.POST.get('dob')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card_type = request.POST.get('card_type')
        ccnsg_passport = request.FILES.get('ccnsg_passport')
        tica_certificates = request.FILES.get('tica_certificates')
        asbestos_certificate = request.FILES.get('asbestos_certificate')
        photo = request.FILES.get('photo')
        dob = datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
        reggno = generate_unique_registration_no()
        
        application = Application(
                name=name,
                address=address,
                ni_number=ni_number,
                town_city=town_city,
                dob=dob,
                postcode=postcode,
                phone=phone,
                email=email,
                card_type=card_type,
                ccnsg_passport=ccnsg_passport,
                tica_certificates=tica_certificates,
                asbestos_certificate=asbestos_certificate,
                photo=photo,
                registration_no=reggno,
                slug=slugify(name),
                cardapplyfor = card
        )

        application.save()
        


        subject = 'Thankyou for Registration | Skill Card'
        message = 'Thankyou for Registration'
        recipient_list = [email,'ajay@arabianmedia.ae']
        html_message = f'''
    <div style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h1 style="color: #333;">Thank You for Registering!</h1>
        <p>Dear {name},</p>
        <p>Thank you for registering for the Skill Card. We have successfully received your application.</p>
        <p>Here are the details you submitted:</p>
        <ul>
            <li><strong>Name:</strong> {name}</li>
            <li><strong>Address:</strong> {address}</li>
            <li><strong>NI Number:</strong> {ni_number}</li>
            <li><strong>Town/City:</strong> {town_city}</li>
            <li><strong>Date of Birth:</strong> {dob}</li>
            <li><strong>Postcode:</strong> {postcode}</li>
            <li><strong>Phone:</strong> {phone}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Card Type:</strong> {card_type}</li>
        </ul>

        <br><br>
        <h3>Your Registation No.</h3>
        <p style="padding:20px; border: 2px solid gray; margin:40px;">
            {reggno}
        </p>



            <p>If any of the above information is incorrect, please contact us immediately at <a href="mailto:contact@arabianmedia.ae">contact@arabianmedia.ae</a>.</p>
            <p>We will review your application and notify you of the next steps soon.</p>
            <p>Thank you for your interest in the Skill Card.</p>
            <p>Best regards,</p>
            <p>The Skill Card Team</p>
        </div>
    
        
        '''

        try:
            send_mail(
                subject,
                message,  # This is the plain text message
                'ajay@arabianmedia.ae',  # From email address
                recipient_list,
                html_message=html_message  # This is the HTML message
            )
            messages.success(request, 'Email sent successfully.')
        except Exception as e:
            messages.error(request, f'Error sending email: {e}')

            

        messages.success(request, 'Application submitted successfully.')
        return HttpResponse(f'''
            <h1>Successfully Applied for Card</h1>
            <p>Please check your Email Id..........</p>
            <br><br>
            <h3>Your Registation No.</h3>
            <p style="padding:20px; border: 2px solid gray; margin:40px;">
                {reggno}
            </p>
                            

            ''')


        
        
        
        # messages.error(request, f'Error submitting application: {e}')



    return render(request,'applyform.html',{'cards' : card})







def application_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        ni_number = request.POST.get('ni_number')
        town_city = request.POST.get('town_city')
        dob = request.POST.get('dob')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card_type = request.POST.get('card_type')
        ccnsg_passport = request.FILES.get('ccnsg_passport')
        tica_certificates = request.FILES.get('tica_certificates')
        asbestos_certificate = request.FILES.get('asbestos_certificate')
        photo = request.FILES.get('photo')

        try:
            application = Application(
                name=name,
                address=address,
                ni_number=ni_number,
                town_city=town_city,
                dob=dob,
                postcode=postcode,
                phone=phone,
                email=email,
                card_type=card_type,
                ccnsg_passport=ccnsg_passport,
                tica_certificates=tica_certificates,
                asbestos_certificate=asbestos_certificate,
                photo=photo,
                registration_no=generate_unique_registration_no(),
                slug=slugify(name)
            )
            application.save()
            messages.success(request, 'Application submitted successfully.')
            return redirect('success')
        except Exception as e:
            messages.error(request, f'Error submitting application: {e}')

    return render(request, 'application_form.html')




def generate_unique_registration_no():
    return str(uuid.uuid4())





def allcards(request):
    card = cardDetails.objects.all()
    return render(request,'allcards.html',{'cards' : card})




def CardDetails(request,slug):
    card = get_object_or_404(cardDetails, slug=slug)
    return render(request,'carddetails.html',{'i' : card})
