from django.contrib import admin
from .models import ActivityPlace

@admin.register(ActivityPlace)
class ActivityPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
