# Generated by Django 4.2.18 on 2025-02-10 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
