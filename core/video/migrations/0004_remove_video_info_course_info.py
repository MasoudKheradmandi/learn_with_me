# Generated by Django 4.1.3 on 2023-01-15 16:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_is_free_video_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='info',
        ),
        migrations.AddField(
            model_name='course',
            name='info',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
