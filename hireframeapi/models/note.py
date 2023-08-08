from django.db import models
from .job import Job


class Note(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    noteBody = models.TextField()
