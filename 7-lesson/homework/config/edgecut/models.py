from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null = True)
    time_updated = models.DateTimeField(auto_now=True, null = True)
    
    
    def __str__(self):
        return self.title
    
    
class About(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null = True)
    time_updated = models.DateTimeField(auto_now=True, null = True)
    
    
    def __str__(self):
        return self.title
    