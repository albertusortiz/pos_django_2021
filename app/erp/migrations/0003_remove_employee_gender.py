# Generated by Django 3.2 on 2021-04-19 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_employee_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]