# Generated by Django 4.1.4 on 2022-12-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
