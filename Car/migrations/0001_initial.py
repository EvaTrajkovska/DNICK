# Generated by Django 4.1.7 on 2023-06-04 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('max_speed', models.IntegerField()),
                ('colour', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manuf_name', models.CharField(max_length=255)),
                ('webpage', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('oldtimer_friendly', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ManufWorkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.manufacturer')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Fix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('desc', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('fix_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car')),
                ('fix_workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.workshop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.manufacturer'),
        ),
    ]
