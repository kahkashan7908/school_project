# Generated by Django 4.2.6 on 2023-10-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.CharField(default='Python', max_length=200),
            preserve_default=False,
        ),
    ]
