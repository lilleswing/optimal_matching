from django.db import models


class CsvFile(models.Model):
  text = models.TextField()
