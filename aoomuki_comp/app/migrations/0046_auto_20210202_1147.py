# Generated by Django 3.1.5 on 2021-02-02 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20210202_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborater',
            name='listofcompetence',
        ),
        migrations.AddField(
            model_name='listofcompetence',
            name='Collaborater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.collaborater', verbose_name='Collaborateur'),
        ),
    ]
