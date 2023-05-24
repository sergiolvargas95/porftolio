from django.db import models

# Create your models here.
class app_personal_information(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    profession = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    profile_picture = models.CharField(max_length=255)
    curriculum_vitae = models.CharField(max_length=255)

class app_cms(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    img = models.CharField(max_length=255)