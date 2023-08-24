from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

admin.site.register(Book, BookAdmin)