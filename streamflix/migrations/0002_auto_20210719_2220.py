# Generated by Django 3.2.5 on 2021-07-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
