from django.contrib import admin
from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    # a property cannot be both in readonly_fields and in prepopulated_fields
    list_filter = (
        "author",
        "rating",
        "is_bestselling",
    )
    list_display = ("title", "author", "is_bestselling")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
