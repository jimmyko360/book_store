from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # id = models.AutoField()
    # ^ Django will already add this for you
    author = models.CharField(null=True, max_length=255)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    # ^this is a native model method that we override

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"