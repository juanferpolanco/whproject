# Generated by Django 5.2 on 2025-05-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0010_alter_apartmentcity_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='apartmentcity',
            table='apartments_cities',
        ),
        migrations.AlterModelTable(
            name='apartmentcountry',
            table='apartments_countries',
        ),
        migrations.AlterModelTable(
            name='apartmentneighborhood',
            table='apartments_neighborhoods',
        ),
    ]
