from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', "first_name", "date_of_birth", "date_of_death")
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)

