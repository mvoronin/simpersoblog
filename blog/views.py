from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from users.views import AuthorMixin

from .forms import PostModelForm
from .models import Category, Post

User = get_user_model()


class RootView(AuthorMixin, TemplateView):
    template_name = 'root.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ctgs = Category.objects.all().order_by('pk').select_related()
        for ctg in ctgs:
            if ctg.name == 'Poems':
                context['ctg_poems'] = ctg
            elif ctg.name == 'Travel':
                context['ctg_travel'] = ctg
            else:
                context['ctg_stories'] = ctg
        return context


class CategoryView(AuthorMixin, DetailView):
    model = Category
    template_name = 'category.html'

    def head(self, *args, **kwargs):
        last_post = self.object.posts.latest('publication_date')
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': last_post.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()
        return context


class PostCreateView(PermissionRequiredMixin, AuthorMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    template_name = 'post-new.html'


class PostDetailView(AuthorMixin, DetailView):
    model = Post
    template_name = 'post.html'


class PostUpdateView(PermissionRequiredMixin, AuthorMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostModelForm
    template_name = 'post-update.html'


class PostPublishView(PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    fields = ['status']


class PostDeleteView(PermissionRequiredMixin, AuthorMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    template_name = 'post-delete.html'

    def get_success_url(self):
        category_slug = self.object.category.slug
        return reverse('category', args=[category_slug])
