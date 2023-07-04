from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    # id = models.AutoField()
    # ^ Django will already add this for you