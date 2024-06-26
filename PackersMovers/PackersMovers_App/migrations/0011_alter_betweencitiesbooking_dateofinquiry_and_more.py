# Generated by Django 5.0 on 2024-03-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PackersMovers_App', '0010_alter_betweencitiesbooking_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betweencitiesbooking',
            name='dateofinquiry',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='betweencitiesbooking',
            name='orderbookeddate',
            field=models.CharField(default='Not Booked', max_length=20),
        ),
        migrations.AlterField(
            model_name='withincitybooking',
            name='dateofinquiry',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='withincitybooking',
            name='orderbookeddate',
            field=models.CharField(default='Not Booked', max_length=20),
        ),
    ]
