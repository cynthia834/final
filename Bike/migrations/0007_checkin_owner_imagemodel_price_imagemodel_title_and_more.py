# Generated by Django 4.2 on 2024-12-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0006_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
