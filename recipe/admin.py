from django.contrib import admin
from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)
    list_display_links = ("title",)
    list_filter = ('title',)


admin.site.register(Category, CategoryAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', "food_name", "category", "created_at", "updated_at")
    search_fields = ("food_name", "category")
    list_filter = ("food_name", "category")
    list_display_links = ("food_name",)


admin.site.register(Recipe, RecipeAdmin)
