from django.db import models
from core.core import CoreBaseModel

# Create your models here.
PYN_DISPLAY = ['id', 'title', 'user']

class Pyn(CoreBaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="pymages")
    user = models.ForeignKey("users.CustomUser", blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField("pyns.Tag", blank=True)