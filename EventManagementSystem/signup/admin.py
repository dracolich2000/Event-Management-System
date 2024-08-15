from django.contrib import admin

# Register your models here.
from signup.models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')

admin.site.register(Signup,SignupAdmin)