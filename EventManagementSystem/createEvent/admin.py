from django.contrib import admin

# Register your models here.
from createEvent.models import CreateEvent

class CreateEventAdmin(admin.ModelAdmin):
    list_display = ('event_name','date','location','description','img')

admin.site.register(CreateEvent,CreateEventAdmin)