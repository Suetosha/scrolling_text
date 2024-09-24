from django.db import models


class VideoText(models.Model):
    text = models.CharField(max_length=200)
