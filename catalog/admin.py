from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author")
  
admin.site.register(Book, BookAdmin)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)