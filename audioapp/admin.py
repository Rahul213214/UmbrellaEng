from django.contrib import admin
from .models import Topic, Conversation

# Register the Topic model
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conver_name',)