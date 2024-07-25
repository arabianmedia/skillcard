
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class cardDetails(models.Model):
    meta_title = models.CharField(max_length=500,null=True,blank=True)
    meta_decription = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255)
    validity = models.CharField(max_length=255)
    decriptions = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True, blank=True)
    democard = models.FileField(upload_to='uploads/dummycard/', blank=True, null=True)

    def __str__(self):
        return self.title
    





class Application(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ni_number = models.CharField(max_length=10)  # Adjust max_length if needed
    town_city = models.CharField(max_length=100)
    dob = models.DateField()  # Storing date as DateField
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    card_type = models.CharField(max_length=50)
    
    # Uploads Section
    ccnsg_passport = models.FileField(upload_to='uploads/ccnsg_passports/', blank=True, null=True)
    tica_certificates = models.FileField(upload_to='uploads/tica_certificates/', blank=True, null=True)
    asbestos_certificate = models.FileField(upload_to='uploads/asbestos_certificates/', blank=True, null=True)
    
    # Application Photo Section
    photo = models.ImageField(upload_to='uploads/photos/', blank=True, null=True)
    
    # New Fields
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    registration_no = models.CharField(max_length=50, unique=True)

    #certificate 
    skillcard = models.FileField(upload_to='uploads/skillcard/', blank=True, null=True)
    slug = models.SlugField(blank=True)

    cardapplyfor = models.ForeignKey(cardDetails, on_delete=models.CASCADE)

    # card details 


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.registration_no:
            last_application = Application.objects.order_by('-id').first()
            if last_application:
                last_id = last_application.id
            else:
                last_id = 0
            self.registration_no = f'APP-{last_id + 1}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')





