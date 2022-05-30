from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

from .models import Category, Post, Comment


class PostAdminForm(forms.ModelForm):
    """ckeEditor"""
    text_ru = forms.CharField(label=_('Post title text[ru]'), widget=CKEditorUploadingWidget())
    text_en = forms.CharField(label=_('Post title text[en]'), widget=CKEditorUploadingWidget())
    description_ru = forms.CharField(label=_('Post description[ru]'), widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label=_('Post description[en]'), widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Admin category"""
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    """Admin post"""
    list_display = ('title', 'created', 'author', 'status', 'category',)
    list_filter = ('title', 'created', 'status')
    search_fields = ('title', 'text')
    list_editable = ('status', 'category')
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin Comment"""
    list_display = ('text', 'author', 'created', 'is_active')
    list_filter = ('created', 'author', 'is_active')
    search_fields = ('text', 'author', 'created', 'is_active')
