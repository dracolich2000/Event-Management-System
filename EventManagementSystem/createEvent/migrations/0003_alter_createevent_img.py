# Generated by Django 5.1 on 2024-08-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createEvent', '0002_alter_createevent_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='img',
            field=models.ImageField(upload_to='media/event_images/'),
        ),
    ]
