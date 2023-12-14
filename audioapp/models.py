from django.db import models
import os


class Topic(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

def audio_file_path(instance, filename):
    base_directory = 'Topics_folder'

    if instance.topic:
        topic_name = instance.topic.name
    else:
        topic_name = 'uncategorized'  # Default folder name if no topic is set

    dynamic_path = os.path.join(base_directory, topic_name)

    # Find the existing conversations for the same topic
    existing_conversations = Conversation.objects.filter(topic=instance.topic)

    # Calculate the next folder number based on the number of existing conversations
    new_folder_number = existing_conversations.count() + 1

    # Adjust the filename to avoid overwriting existing files
    file_path = os.path.join(dynamic_path, f"conversation_{new_folder_number}", filename)
    return file_path

class Conversation(models.Model):
    conver_name = models.CharField(max_length=200)
    folder_number = models.IntegerField(default=0, editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    audio_file1 = models.FileField(upload_to=audio_file_path)
    audio_file2 = models.FileField(upload_to=audio_file_path)
    audio_file3 = models.FileField(upload_to=audio_file_path)

    def __str__(self):
        return str(self.conver_name)  # Display the file name or customize as needed
