from django import forms

from .models import Contact
from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """Contact us form"""
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'captcha')
