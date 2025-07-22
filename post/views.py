from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
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


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if request.user.is_authenticated and form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect('post_by_slug', slug=self.object.slug)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/edit_comment.html'

    def get_success_url(self):
        return reverse('post_by_slug', kwargs={'slug': self.object.post.slug})

    def test_func(self):
        return self.request.user == self.get_object().user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'post/delete_comment.html'

    def get_success_url(self):
        return reverse('post_by_slug', kwargs={'slug': self.object.post.slug})

    def test_func(self):
        return self.request.user.is_superuser
