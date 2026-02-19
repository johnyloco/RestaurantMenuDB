from django.contrib import admin

from drinks.models import Drink, Wine


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')
    list_filter = ('title', 'description', 'price', 'category')
    search_fields = ('title', 'description', 'price', 'category')

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')
    list_filter = ('title', 'description', 'price', 'category')
    search_fields = ('title', 'description', 'price', 'category')

