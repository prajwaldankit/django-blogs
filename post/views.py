from django.views.generic import DetailView
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.


def index(request):
    posts = Post.objects.all().select_related('category')
    return render(request, 'post/home.html', {
        'posts': posts
    })


def post_detail_by_id(request, id):
    post = Post.objects.select_related('category').get(pk=id)
    return render(request, 'post/post_detail.html', {
        "id": id,
        "post": post
    })


def post_detail_by_slug(request, slug):
    post = Post.objects.select_related('category').get(slug=slug)
    return render(request, 'post/post_detail.html', {
        "id": post.pk,
        "post": post
    })


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        # TODO: implement saving comments.
        return None
