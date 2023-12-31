# Generated by Django 5.0 on 2023-12-14 11:45

import audioapp.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0005_conversation_folder_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='topi_description',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='topic_name',
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AudioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to=audioapp.models.audio_file_path)),
                ('folder_number', models.IntegerField(default=0, editable=False)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audioapp.topic')),
            ],
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
