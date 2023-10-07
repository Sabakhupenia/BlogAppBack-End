from django.contrib import admin
from .models import BlogPost
from Readinglist.models import Category, Topic, Author


admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Author)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    fields = ('title', 'content', 'author', 'categories', 'topics')
