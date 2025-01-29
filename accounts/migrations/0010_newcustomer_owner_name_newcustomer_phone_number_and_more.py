# Generated by Django 4.2.18 on 2025-01-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_newcustomer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcustomer',
            name='owner_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newcustomer',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='income',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
