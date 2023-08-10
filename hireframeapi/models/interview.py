from django.db import models


class Interview(models.Model):
    seeker = models.ForeignKey("Seeker", on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField()
