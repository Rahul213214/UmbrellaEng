# Generated by Django 5.0 on 2023-12-14 11:56

import audioapp.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0008_rename_audio_file_audiomodel_audio_file1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='name',
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_name', models.CharField(max_length=200)),
                ('audiofile1', models.FileField(upload_to=audioapp.models.audio_file_path)),
                ('audiofile2', models.FileField(upload_to=audioapp.models.audio_file_path)),
                ('audiofile3', models.FileField(upload_to=audioapp.models.audio_file_path)),
                ('audiofile4', models.FileField(upload_to=audioapp.models.audio_file_path)),
                ('conversation_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioapp.topic')),
            ],
        ),
        migrations.DeleteModel(
            name='AudioModel',
        ),
    ]