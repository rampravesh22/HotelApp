# Generated by Django 4.0.5 on 2022-07-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_hotelimages_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='amenities',
            field=models.ManyToManyField(related_name='hotel_amenities', to='home.amenities'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='booking_type',
            field=models.CharField(choices=[('Pre Paid', 'Prepaid'), ('Post Paid', 'Postpaid')], max_length=100),
        ),
    ]
