# Generated by Django 5.1.3 on 2024-12-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicycle',
            name='description',
        ),
        migrations.AddField(
            model_name='bicycle',
            name='time_taken',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
