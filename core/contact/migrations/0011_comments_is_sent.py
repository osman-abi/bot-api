# Generated by Django 4.0 on 2022-04-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_remove_comments_is_sent_alter_commentauthors_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
