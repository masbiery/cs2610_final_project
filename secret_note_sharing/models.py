from __future__ import unicode_literals
import uuid

from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.message_text

