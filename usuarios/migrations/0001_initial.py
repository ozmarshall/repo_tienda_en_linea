# Generated by Django 4.0.3 on 2022-05-27 19:26

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('name', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('alias', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('document', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('confirmpassword', models.TextField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]