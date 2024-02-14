from django.contrib import admin
from pyns.models import *

# Register your models here.

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = LIKES_DISPLAY