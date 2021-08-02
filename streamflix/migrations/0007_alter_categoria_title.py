# Generated by Django 3.2.5 on 2021-08-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamflix', '0006_alter_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='title',
            field=models.CharField(choices=[('E', 'Entrepreneurship'), ('F', 'Finances'), ('G', 'Games'), ('H', 'healthy'), ('M', 'Movies'), ('N', 'Nerd'), ('P', 'Programming'), ('SER', 'Series'), ('TEC', 'Technology'), ('TRI', 'Trips')], default='P', max_length=3),
        ),
    ]
