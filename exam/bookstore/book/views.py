from django.shortcuts import render, get_object_or_404
from .models import Home,Category,GroupPost,Book


categories = Category.objects.all()
groups = GroupPost.objects.all()
home = Home.objects.all()
books = Book.objects.all().values()
# Create your views here.
def index(request):
    data = {
        'home':home,
        'categories':categories,
        'groups':groups,
        'books':books
    }
    return render(request, 'book/index.html', context=data)


def subpage(request, post_slug):
    book = get_object_or_404(Book, slug=post_slug)
    data = {
        'home':home,
        'categories':categories,
        'groups':groups,
        'book':book
    }
    return render(request, 'book/subpage.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    books = category.books.filter(in_stock=1)
    data = {
        'books':books,
        'categories':categories,
        'groups':groups
    }
    
    return render(request, 'book/index.html', context=data)

def show_group(request, guruh_slug):
    group = get_object_or_404(GroupPost, slug=guruh_slug)
    books = group.group_book.filter(in_stock=True)
    data = {
        'books':books,
        'categories':categories,
        'groups':groups
    }
    
    return render(request, 'book/index.html', context=data)