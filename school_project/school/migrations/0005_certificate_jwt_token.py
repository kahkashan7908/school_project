# Generated by Django 4.2.6 on 2023-10-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='jwt_token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]