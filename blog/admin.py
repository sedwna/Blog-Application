from django.contrib import admin
from .models import Post  # *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published')
    ordering = ('-published',)
    list_filter = ('status','author')
    search_fields = ('title','description')
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    # list_display_links = ('title',)