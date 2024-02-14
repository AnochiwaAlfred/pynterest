from django.db import models
from core.core import CoreBaseModel

# Create your models here.
SAVED_PYN_DISPLAY = ['id', 'user', 'pyn']
class SavedPyn(CoreBaseModel):
    pyn = models.ForeignKey('pyns.Pyn', related_name='saved_pyns', null=True, blank=True, on_delete=models.CASCADE)    
    user = models.ForeignKey("users.CustomUser", blank=True, null=True, on_delete=models.CASCADE)