# Generated by Django 3.2 on 2021-11-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0005_remove_photos_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]