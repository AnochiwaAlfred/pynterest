from django.contrib import admin
from pyns.models import *

# Register your models here.

@admin.register(SavedPyn)
class SavedPynAdmin(admin.ModelAdmin):
    list_display = SAVED_PYN_DISPLAY