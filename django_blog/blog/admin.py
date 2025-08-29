from django.contrib import admin
from .models import post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "published_date", "author")
    search_fields = ("title",)


admin.site.register(post,PostAdmin)