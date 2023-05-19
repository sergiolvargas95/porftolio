from django.db import models

# creation of the information model || table
class Information(models.Model):
    Name = models.TextField(max_length=250)
    LastName = models.TextField(max_length=250)
    Profession = models.TextField(max_length=250)
    Description = models.TextField(max_length=250)
    profilePicture = models.TextField(max_length=255)
    curriculumVitae = models.TextField(max_length=255)

#creation of the App_cms model || table
class App_cms(models.Model):
    Name = models.TextField(max_length=250)
    title = models.TextField(200)
    img = models.TextField(250)