# Generated by Django 2.1 on 2021-01-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_collaborater_society'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborater',
            name='Society',
        ),
        migrations.AddField(
            model_name='collaborater',
            name='society',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Society'),
        ),
        migrations.AlterField(
            model_name='collaborater',
            name='workstation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ListWorkStation'),
        ),
    ]
