from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # id = models.AutoField()
    # ^ Django will already add this for you
    author = models.CharField(null=True, max_length=255)
    is_bestselling = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book_by_id", args=[self.id])
    # ^this is a native model method that we override

    def __str__(self):
        return f"{self.title} ({self.rating})"