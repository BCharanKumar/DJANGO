# Generated by Django 5.0.7 on 2024-10-19 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='charanbkumar25@gmail.com', max_length=254),
        ),
    ]