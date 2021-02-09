from django.contrib import admin

from .models import Comment, Tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "text", )


admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)
