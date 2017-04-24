from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.question_text

