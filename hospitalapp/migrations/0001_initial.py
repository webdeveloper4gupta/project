# Generated by Django 4.0.3 on 2022-04-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('id_no', models.PositiveIntegerField()),
                ('email', models.EmailField(default=None, max_length=70)),
                ('password', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('phno', models.CharField(max_length=80)),
                ('email', models.EmailField(default=None, max_length=80)),
                ('Disease', models.CharField(max_length=700)),
                ('Description', models.TextField(max_length=900)),
            ],
        ),
    ]
