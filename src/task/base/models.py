from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.

class task(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['done']
        