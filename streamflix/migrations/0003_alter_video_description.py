# Generated by Django 3.2.5 on 2021-07-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamflix', '0002_auto_20210719_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
