# Generated by Django 5.0.1 on 2024-02-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_activation_token_expire_profile_confirmation_code_expire_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='confirmation_code_expire',
            new_name='activation_token_expire',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='confirmation_code',
        ),
        migrations.AddField(
            model_name='profile',
            name='activation_token',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
