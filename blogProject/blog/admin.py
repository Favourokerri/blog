from django.contrib import admin
from .models import Category, BlogPost, NewsLetter, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category',]

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at']
    ordering = ['-updated_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(NewsLetter)
