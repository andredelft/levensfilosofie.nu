from django.db import models


class Symposium(models.Model):
    titel = models.CharField(max_length=300)
    aankondiging = models.TextField()
    date = models.DateField()
