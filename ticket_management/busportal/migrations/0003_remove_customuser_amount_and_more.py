# Generated by Django 5.0.7 on 2024-07-14 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busportal', '0002_userdetails_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='time_stamp',
        ),
    ]
