from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_id', 'category', 'publish_date', 'last_published')


admin.site.register(Post, PostAdmin)
