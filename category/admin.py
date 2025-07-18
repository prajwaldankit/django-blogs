from django.contrib import admin
from .models import Category


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # exclude = ('slug',)
    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
