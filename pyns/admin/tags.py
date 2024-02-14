from django.contrib import admin
from pyns.models import *

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = TAG_DISPLAY