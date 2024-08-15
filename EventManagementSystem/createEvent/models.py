from django.db import models
from signup.models import Signup

# Create your models here.
class CreateEvent(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    img = models.ImageField(upload_to='event_images/')
    username = models.ForeignKey(Signup, on_delete=models.CASCADE,null=True)