# Generated by Django 2.1.2 on 2019-04-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_adress',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_city',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='iframe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
