# Generated by Django 4.2.3 on 2024-12-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='royxta',
            name='royxat_vaqti',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
