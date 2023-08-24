from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    # a property cannot be both in readonly_fields and in prepopulated_fields

admin.site.register(Book, BookAdmin)