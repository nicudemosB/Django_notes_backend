from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    # //line 8 creates a time stamp of when the note was created//
    updated = models.DateTimeField(auto_now=True)
    # //auto now add: takes a time stamp on creation of the model
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]