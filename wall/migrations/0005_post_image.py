# Generated by Django 3.2 on 2021-05-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_auto_20210528_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='posts/'),
        ),
    ]