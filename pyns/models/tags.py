from django.db import models
from core.core import CoreBaseModel

# Create your models here.
TAG_DISPLAY = ['id', 'title']
class Tag(CoreBaseModel):
    title = models.CharField(max_length=255, null=True, blank=True, unique=True)