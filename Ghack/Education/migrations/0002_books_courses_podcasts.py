# Generated by Django 5.0 on 2024-02-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('podcast_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
