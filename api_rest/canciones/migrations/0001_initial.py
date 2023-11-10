# Generated by Django 4.2.7 on 2023-11-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('artista', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('año_lanzamiento', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
    ]
