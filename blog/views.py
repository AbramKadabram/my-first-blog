from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post , Product

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def shop_list(request):
    shops = Product.objects.all()
    return render(request, 'shop/shop_list.html', {'shops': shops})

def shop_detail(request, pk):
    shop = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/shop_detail.html', {'shop': shop})
