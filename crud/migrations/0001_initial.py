# Generated by Django 3.1.1 on 2020-10-06 10:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Maker (eg.BMW)', max_length=50, validators=[django.core.validators.MinLengthValidator(3, 'Must be greater than 2 Characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.make')),
            ],
        ),
    ]
