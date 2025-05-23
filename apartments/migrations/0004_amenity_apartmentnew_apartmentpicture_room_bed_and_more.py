# Generated by Django 5.2 on 2025-05-09 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_apartment_imagepath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('currency', models.CharField(max_length=10)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cleaning_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('bathrooms', models.IntegerField()),
                ('accommodates', models.IntegerField()),
                ('public_summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='apartments.apartmentnew')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='apartments.apartmentnew')),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='apartments.room')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentAmenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.amenity')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment_amenities', to='apartments.apartmentnew')),
            ],
            options={
                'unique_together': {('apartment', 'amenity')},
            },
        ),
    ]
