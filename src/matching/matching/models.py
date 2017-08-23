from django.db import models


class CsvFile(models.Model):
  text = models.TextField()
  created = models.DateTimeField(auto_now_add=True, blank=True)
