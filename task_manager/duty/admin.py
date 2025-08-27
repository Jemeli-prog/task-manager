from django.contrib import admin
from .models import Duty

@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ('title','is_done')
    list_filter = ('is_done',)
    search_fields = ('title', 'description')

# Register your models here.
