# Generated by Django 2.2.7 on 2020-02-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdDetection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.TextField()),
                ('joy', models.FloatField()),
                ('sorrow', models.FloatField()),
                ('anger', models.FloatField()),
                ('surprise', models.FloatField()),
                ('like_factor', models.FloatField()),
            ],
        ),
    ]
