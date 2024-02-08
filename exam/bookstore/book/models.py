from django.db import models



# Asosiy page modeli
class Home(models.Model):
    bg_image = models.CharField(max_length=255)
    content1 = models.TextField(blank=True)
    li1 = models.TextField(blank=True)
    li2 = models.TextField(blank=True)
    li3 = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.bg_image


# Adabiyot modeli
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True) 
    
    def __str__(self) -> str:
        return self.name
    
    

# Guruhlar modeli
class GroupPost(models.Model):
    group_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    
    def __str__(self) -> str:
        return self.group_name
    

# Kitoblar modeli
class Book(models.Model):
    img_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)   
    time_update = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'books')
    group = models.ManyToManyField('GroupPost', blank=True, related_name='group_book')
    
    def __str__(self) -> str:
        return self.name