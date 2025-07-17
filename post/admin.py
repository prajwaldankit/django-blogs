from django.contrib import admin
from .models import Post


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    readonly_fields = ('slug',)


admin.site.register(Post, PostAdmin)
