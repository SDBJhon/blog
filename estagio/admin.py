from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "status")
    list_filter = ("status", "created", "published",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "contents")
    date_hierarchy = "published"
    raw_id_fields = ("author",)
