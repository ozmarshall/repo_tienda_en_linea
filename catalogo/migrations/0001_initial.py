# Generated by Django 4.0.4 on 2022-05-25 20:44

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
                ('numberItem', models.CharField(max_length=45)),
                ('contac', models.CharField(max_length=45)),
                ('phoneNumber', models.CharField(max_length=45)),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('paymentMeth', models.CharField(max_length=45)),
                ('receptionN', models.CharField(max_length=45)),
                ('stateRanking', models.CharField(max_length=45)),
                ('stateS', models.IntegerField()),
                ('tittle', models.CharField(max_length=45)),
                ('typeCurrency', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
    ]
