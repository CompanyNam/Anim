# Generated by Django 2.1.2 on 2019-06-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_event_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
