from django.shortcuts import render, get_object_or_404

from posts.models import Post


def home(request):
    context = {}
    context['all_posts'] = list(Post.objects.all().order_by('-pub_date'))
    return render(request, 'posts/home.html', context)


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_details.html', {'post': post})


def about(request):
    return render(request, 'posts/about.html')
