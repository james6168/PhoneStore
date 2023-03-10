# Generated by Django 4.1.6 on 2023-02-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartphoneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='smartphones')),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_camera_mp', models.PositiveSmallIntegerField()),
                ('wide_camera_mp', models.PositiveSmallIntegerField()),
                ('front_camera_mp', models.PositiveSmallIntegerField()),
                ('specs', models.TextField()),
                ('extra', models.TextField()),
                ('operating_system', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=50)),
                ('grafical_processor', models.CharField(max_length=50)),
                ('dynamic', models.CharField(max_length=50)),
                ('accumulator', models.PositiveSmallIntegerField()),
                ('sim_count', models.PositiveSmallIntegerField()),
                ('ssd', models.PositiveSmallIntegerField()),
                ('ram', models.PositiveSmallIntegerField()),
                ('external_ssd', models.BooleanField()),
                ('display_size', models.PositiveSmallIntegerField()),
                ('display_type', models.CharField(max_length=50)),
                ('display_resolution', models.CharField(max_length=50)),
                ('case', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('is_available', models.BooleanField()),
                ('description', models.TextField()),
                ('images', models.ManyToManyField(blank=True, to='smartphones.smartphoneimage')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('smartphones', models.ManyToManyField(blank=True, to='smartphones.smartphone')),
            ],
        ),
    ]
