# Generated by Django 3.1.5 on 2021-02-18 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20210218_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborater',
            old_name='profil',
            new_name='UserProfil',
        ),
    ]
