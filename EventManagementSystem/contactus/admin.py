from django.contrib import admin

# Register your models here.
from contactus.models import Contactus

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(Contactus,ContactusAdmin)