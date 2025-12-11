from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog

# trigger signal before saving a blog
@receiver(pre_save, sender=Blog)
def blog_before_save(sender, instance, **kwargs):
    print(f'About to save blog [Pre_Save]: {instance.title}')

# trigger signal after saving a blog
@receiver(post_save, sender=Blog)
def blog_after_save(sender, instance, created, **kwargs):
    if created:
        print(f'New blog created [Post_Save]: {instance.title}')
    else:
        print(f'Blog updated [Post_Save]: {instance.title}')
