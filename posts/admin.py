from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_id', 'category', 'publish_date', 'last_published')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
