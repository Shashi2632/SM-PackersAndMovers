# Generated by Django 5.0 on 2024-01-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PackersMovers_App', '0005_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='betweencitiesbooking',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AddField(
            model_name='withincitybooking',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]