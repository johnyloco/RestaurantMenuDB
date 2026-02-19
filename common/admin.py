from django.contrib import admin

from common.models import Allergy


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
