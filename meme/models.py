from django.db import models

# Create your models here.
class Meme(models.Model):
    name=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)
    url = models.URLField(max_length = 200) 
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date',]
