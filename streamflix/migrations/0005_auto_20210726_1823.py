# Generated by Django 3.2.5 on 2021-07-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamflix', '0004_alter_video_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('E', 'Entrepreneurship'), ('F', 'Finances'), ('G', 'Games'), ('H', 'healthy'), ('M', 'Movies'), ('N', 'Nerd'), ('P', 'Programming'), ('S', 'Series'), ('T', 'Technology'), ('O', 'Trips')], default='P', max_length=1)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
