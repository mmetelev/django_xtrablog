from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.translation import gettext_lazy as _

from .models import *


class PostAdminForm(forms.ModelForm):
    """ckeEditor"""
    text = forms.CharField(label=_('Text about'), widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


@admin.register(About)
class AdminContact(TranslationAdmin):
    """About us"""
    list_display = ('image', 'location', 'phone_number', 'email_blog', 'text')


@admin.register(Team)
class AdminContact(TranslationAdmin):
    """Team blog"""
    list_display = ('image', 'name', 'position')


@admin.register(Contact)
class AdminContact(TranslationAdmin):
    """Contact Us"""
    list_display = ('name', 'email', 'subject', 'message')


@admin.register(Card)
class AdminCard(TranslationAdmin):
    """Card in about section"""
    list_display = ('title', 'text')
