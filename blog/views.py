from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    """All posts in the list"""
    paginate_by = 4
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status='published')


class CategoryListView(ListView):
    """List of categories"""
    paginate_by = 4
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    """Detail post"""
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    new_public = Post.objects.order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['tag_list'] = self.object.tags.similar_objects()[:3]
        return context


class AddCommentView(CreateView):
    """Add and save comment in detail post"""
    model = Comment
    form_class = CommentForm
    object = None

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class SearchResultsView(ListView):
    """Search results from a form """
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
