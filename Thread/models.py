from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    participant1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads_started')
    participant2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads_involved')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('participant1', 'participant2')


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    text = models.CharField(max_length=1000)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
