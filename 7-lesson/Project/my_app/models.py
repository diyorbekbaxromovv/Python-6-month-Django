from django.db import models

# Create your models here.

class Image(models.Model):
    img_name = models.CharField(max_length=255)
    description = models.TextField()
    
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time_created = models.DateField(auto_now_add=True, null=True)
    time_updated = models.DateField(auto_now=True, null=True)
    
    
def __str__(self):
    return self.title