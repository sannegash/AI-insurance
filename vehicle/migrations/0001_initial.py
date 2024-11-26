# Generated by Django 5.1.2 on 2024-11-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_firstname', models.CharField(help_text=' first name of driver ', max_length=100)),
                ('driver_lastname', models.CharField(help_text=' last name of driver ', max_length=100)),
                ('licence_number', models.CharField(help_text='drivers licence number', max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(help_text='Unique vehicle registration number.', max_length=15, unique=True)),
                ('owner_name', models.CharField(help_text='Name of the vehicle owner.', max_length=100)),
                ('vehicle_make', models.CharField(help_text='Brand of the vehicle (e.g., Toyota).', max_length=50)),
                ('vehicle_model', models.CharField(help_text='Model of the vehicle (e.g., Corolla).', max_length=50)),
                ('vehicle_year', models.PositiveIntegerField(help_text='Year the vehicle was manufactured.')),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], help_text='Fuel type of the vehicle.', max_length=10)),
                ('transmission_type', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], help_text='Transmission type of the vehicle.', max_length=10)),
                ('engine_capacity', models.DecimalField(decimal_places=1, help_text='Engine capacity in liters (e.g., 2.0 for a 2000cc engine).', max_digits=4)),
                ('color', models.CharField(help_text='Color of the vehicle.', max_length=30)),
                ('chassis_number', models.CharField(help_text="Unique identifier for the vehicle's chassis.", max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the vehicle was added.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the vehicle was last updated.')),
            ],
        ),
    ]
