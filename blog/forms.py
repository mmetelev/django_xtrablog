from django import forms

from .models import Comment
from captcha.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    """Comments in post detail"""
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('author', 'email', 'text', 'captcha')
        widgets = {
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'text': forms.Textarea(attrs={"rows": 6, "class": "form-control"}),
        }
