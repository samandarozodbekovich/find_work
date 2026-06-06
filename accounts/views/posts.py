from django.shortcuts import get_object_or_404, redirect
from django.db.models import F
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView

from ..models import Post
from ..forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'accounts/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'accounts/post_detail.html'
    context_object_name = 'post'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hitinfo = context.get('hitcount', {})
        # only increment Post.views when hitcount actually recorded a hit
        if hitinfo.get('hit_counted'):
            Post.objects.filter(pk=self.object.pk).update(views=F('views') + 1)
            self.object.refresh_from_db()
            context['post'] = self.object
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'accounts/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        if 'add_another' in self.request.POST:
            return redirect('add_post', user_pk=self.request.user.pk)
        return redirect('post_detail', post.pk)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'accounts/post_form.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form):
        post = form.save()
        return redirect('post_detail', post.pk)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'accounts/confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_pk': self.request.user.pk})

