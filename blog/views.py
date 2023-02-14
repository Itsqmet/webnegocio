from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.

def blog(request):
    blogs= Blog.objects.all()
    return render(request, "blog/blog.html", {'blogs': blogs})
    
def category(request, category_id):
    #category=Category.objects.get(id=category_id)
    category= get_object_or_404(Category, id=category_id)
    #tomat los blog que le pertenece a esa categoria
    blogs=Blog.objects.filter(categories=category)
    return render(request, "blog/category.html", {'blogs':blogs})
