# Generated by Django 4.0 on 2022-04-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_replymessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
