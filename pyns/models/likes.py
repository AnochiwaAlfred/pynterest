from django.db import models

from core.core import CoreBaseModel

# Create your models here.


LIKES_DISPLAY = ['id', 'user', 'pyn']
class Likes(CoreBaseModel):
    user = models.ForeignKey('users.CustomUser', null=True, blank=True,  on_delete=models.CASCADE)
    pyn = models.ForeignKey('pyns.Pyn', related_name='likes', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.pyn}"
    
    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        