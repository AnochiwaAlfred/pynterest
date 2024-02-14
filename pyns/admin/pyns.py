from django.contrib import admin
from pyns.models import *

# Register your models here.

@admin.register(Pyn)
class PynAdmin(admin.ModelAdmin):
    list_display = PYN_DISPLAY