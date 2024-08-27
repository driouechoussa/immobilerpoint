# Generated by Django 5.0.7 on 2024-08-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='immobiler_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_address', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_images', models.ImageField(blank=True, upload_to='')),
                ('product_bathrooms', models.IntegerField(default=2)),
                ('product_bedrooms', models.IntegerField(default=2)),
                ('product_guests', models.IntegerField(default=2)),
                ('product_area', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
