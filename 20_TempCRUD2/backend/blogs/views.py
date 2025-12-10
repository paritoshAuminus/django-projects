from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blogs/post_create.html'
    fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blogs/post_create.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/post_delete.html'
    reverse_lazy('post_list')