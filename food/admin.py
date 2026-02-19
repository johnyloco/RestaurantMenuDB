from django.contrib import admin

from food.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')
    list_filter = ('title', 'description', 'price', 'category')
    search_fields = ('title', 'description', 'price', 'category')
