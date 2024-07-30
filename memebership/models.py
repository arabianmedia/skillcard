from django.db import models




class Membership(models.Model):
    metatag = models.CharField(max_length=255)
    metadescription = models.TextField()
    title = models.CharField(max_length=255)
    shortdescription = models.TextField()
    longdescription = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

class MembershipApplication(models.Model):
    company_name = models.CharField(max_length=255)
    asbestos_removal = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    
    training_contact_name = models.CharField(max_length=255)
    training_contact_email = models.EmailField()

    audit_contact_name = models.CharField(max_length=255, blank=True, null=True)
    audit_contact_email = models.EmailField(blank=True, null=True)

    marketing_contact_name = models.CharField(max_length=255, blank=True, null=True)
    marketing_contact_email = models.EmailField(blank=True, null=True)

    regional_contact_name = models.CharField(max_length=255, blank=True, null=True)
    regional_contact_email = models.EmailField(blank=True, null=True)

    accounts_contact_name = models.CharField(max_length=255, blank=True, null=True)
    accounts_contact_email = models.EmailField(blank=True, null=True)

    additional_telephone = models.CharField(max_length=20, blank=True, null=True)
    additional_postcode = models.CharField(max_length=20, blank=True, null=True)
    company_reg_no = models.CharField(max_length=50)
    vat_reg_no = models.CharField(max_length=50)

    signature = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date = models.DateField()

    health_safety_statement = models.FileField(upload_to='documents/')
    liability_insurance = models.FileField(upload_to='documents/')
    company_registration = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.company_name

    