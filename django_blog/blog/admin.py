from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "published_date", "author")
    search_fields = ("title",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "content", "created_at", "updated_at")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post,PostAdmin)