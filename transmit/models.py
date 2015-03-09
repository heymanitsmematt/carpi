from django.db import models

class Files(models.Model):
    file_name = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    times_played = models.IntegerField(null=True)
