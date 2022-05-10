from django.db import models

# Create your models here.
class Certificate(models.Model):
    title = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    source = models.CharField(max_length=20) # i.e. Codecademy
    link = models.URLField(max_length=200)
    cert_image = models.CharField(max_length=100)