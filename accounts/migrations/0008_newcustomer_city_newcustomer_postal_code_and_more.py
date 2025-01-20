# Generated by Django 4.2.18 on 2025-01-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_newcustomer_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcustomer',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newcustomer',
            name='postal_code',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newcustomer',
            name='state',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
