from django.db import models
from django.contrib.auth.models import User 

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Notes'
        