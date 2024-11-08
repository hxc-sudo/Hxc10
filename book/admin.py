from django.contrib import admin
from .models import Book, BookReview
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    # list_editable = ('description','title')

admin.site.register(Book, BookAdmin)
admin.site.register(BookReview)