from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager


class Category(models.Model):
    """Category Model"""
    title = models.CharField(verbose_name=_('Category title'), max_length=150)
    slug = models.SlugField(verbose_name=_('Category URL'), max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category'),
        verbose_name_plural = _("Category's")


class Post(models.Model):
    """Post Model"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    image = models.ImageField(verbose_name=_('Post image'), upload_to='images/%Y/%m/%d')
    video = models.FileField(
        verbose_name=_('Post video'),
        upload_to='video/%Y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        blank=True,
        null=True
    )
    title = models.CharField(verbose_name=_('Post name'), max_length=100)
    text = models.TextField(verbose_name=_('Text in post list'), max_length=360)
    description = models.CharField(verbose_name=_('Full post text'), max_length=2000)
    tags = TaggableManager()
    created = models.DateTimeField(verbose_name=_('Post creation date'), auto_now_add=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_('Post category'),
        related_name='post',
        on_delete=models.SET_NULL,
        null=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name=_('Post author'),
        related_name='posts',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        verbose_name=_('Visible status'),
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    is_new = models.BooleanField(verbose_name=_('New post indicator'), default=False)
    slug = models.SlugField(verbose_name=_('Post URL'), max_length=250, unique_for_date='created')

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Post'),
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_comments(self):
        return self.comment.all()

    def get_comments_count(self):
        return self.comment.count()


class Comment(models.Model):
    """Comment Model"""
    image = models.ImageField(verbose_name=_('User image'), upload_to='comment')
    author = models.CharField(verbose_name=_('Authors name'), max_length=50)
    text = models.TextField(verbose_name=_('Comment text'), max_length=500)
    created = models.DateTimeField(verbose_name=_('Comment creation date'), auto_now_add=True)
    email = models.EmailField(verbose_name=_('User email'), max_length=100)
    post = models.ForeignKey(
        Post,
        verbose_name=_('Relevant post'),
        related_name='comment',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(verbose_name=_('Comment visibility'), default=True)
    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent comment'),
        related_name='replies',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('created',)
        verbose_name = _('Comment'),
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.author
