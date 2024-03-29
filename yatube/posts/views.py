from django.shortcuts import render, get_object_or_404

from .models import Post, Group
from yatube.settings import NOTES_NUMBER


def index(request):
    posts = Post.objects.all()[:NOTES_NUMBER]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NOTES_NUMBER]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
