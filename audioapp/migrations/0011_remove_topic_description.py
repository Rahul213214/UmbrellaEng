# Generated by Django 5.0 on 2023-12-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0010_rename_audiofile1_conversation_audio_file1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
    ]