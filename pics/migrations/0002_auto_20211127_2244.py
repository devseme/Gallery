# Generated by Django 3.2 on 2021-11-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='photos',
            name='category',
            field=models.ManyToManyField(to='pics.category'),
        ),
    ]
