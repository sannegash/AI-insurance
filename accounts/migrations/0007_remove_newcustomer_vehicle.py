# Generated by Django 5.1.2 on 2024-12-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_insuredcustomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcustomer',
            name='vehicle',
        ),
    ]