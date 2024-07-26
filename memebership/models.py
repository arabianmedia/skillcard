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