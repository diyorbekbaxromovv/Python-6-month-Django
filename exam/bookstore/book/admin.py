from django.contrib import admin
from .models import Home,Category,GroupPost, Book
# Register your models here.

admin.site.register([Home,Category,GroupPost,Book])