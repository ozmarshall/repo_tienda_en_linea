# Generated by Django 4.0.4 on 2022-05-24 19:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('foto', cloudinary.models.CloudinaryField(max_length=255)),
                ('disponible', models.BooleanField(default=True)),
                ('precio', models.FloatField()),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
    ]
