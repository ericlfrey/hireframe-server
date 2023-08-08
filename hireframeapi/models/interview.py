from django.db import models
from .job import Job


class Interview(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField()
