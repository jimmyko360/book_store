from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # id = models.AutoField()
    # ^ Django will already add this for you
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(
        default="",
        # we no longer need these properties if we use either readonly_fields or prepopulated_fields in admin.py
        # blank=True,
        # editable=False,
        null=False,
        db_index=True,
    )

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # ^this is a native model method that we override

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    # we moved this work to be performed by BookAdmin

    def __str__(self):
        return f"{self.title} ({self.rating})"
