from django.contrib import admin

# Register your models here.
from .models import Information,App_cms

admin.site.register(Information)
admin.site.register(App_cms)