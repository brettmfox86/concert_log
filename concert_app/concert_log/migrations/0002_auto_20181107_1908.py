# Generated by Django 2.1.3 on 2018-11-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
