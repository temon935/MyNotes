from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'created_at', 'is_read', 'review', 'rate')


admin.site.register(Books, BooksAdmin)