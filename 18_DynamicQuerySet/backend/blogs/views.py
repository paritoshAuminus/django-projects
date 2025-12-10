from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q')    # search keywords in url
    category = request.GET.get('category')  # filter category

    post = Post.objects.all()

    # search using Q objects
    if query:
        post = post.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # filter by category
    if category:
        post = post.filter(category__iexact=category)

    return render(request, 'blogs/post_list.html', {
        'post': post, 
        'query': query, 
        'category': category, 
        })
