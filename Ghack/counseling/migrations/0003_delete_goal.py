# Generated by Django 5.0 on 2024-02-23 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counseling', '0002_remove_comment_id_remove_comment_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goal',
        ),
    ]