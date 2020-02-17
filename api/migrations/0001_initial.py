# Generated by Django 3.0.3 on 2020-02-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=20)),
                ('locationText1', models.CharField(max_length=80)),
                ('locationText2', models.CharField(max_length=80)),
                ('locationText3', models.CharField(max_length=80)),
                ('locationText4', models.CharField(max_length=80)),
                ('locLat', models.DecimalField(decimal_places=9, default=None, max_digits=12)),
                ('locLng', models.DecimalField(decimal_places=9, default=None, max_digits=12)),
            ],
        ),
    ]
