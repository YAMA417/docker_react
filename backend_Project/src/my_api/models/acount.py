from django.db import models
from my_api.models import BaseModel

class Acount(BaseModel):
    class Meta:
       db_table = 'acount'
       verbose_name = verbose_name_plural = 'アカウント一覧'
    
    acount_name = models.CharField(
        verbose_name="アカウント名",
        blank=True,
        null=False,
        max_length=255
    )
    
    password = models.UUIDField(
        verbose_name="パスワード",
        blank=True,
        null=False,
        max_length=255
    )
    
    def __str__(self):
    	return self.id
    
    
