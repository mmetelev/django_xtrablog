from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class About(models.Model):
    """About blog & address"""
    image = models.ImageField(verbose_name=_('Hero image'), upload_to='about')
    text = models.TextField(verbose_name=_('Text body'), max_length=500)
    location = models.CharField(verbose_name=_('Blog location'), max_length=200)
    phone_number = models.CharField(verbose_name=_('Blog Tel'), max_length=100)
    email_blog = models.EmailField(verbose_name=_('Blog email'), max_length=50)
    contact_text = models.TextField(verbose_name=_('Additional description of contacts'), max_length=150)

    class Meta:
        verbose_name = _('About'),
        verbose_name_plural = _('Abouts')


class Team(models.Model):
    """About Team"""
    image = models.ImageField(verbose_name=_('Employee photo'), upload_to='employee')
    name = models.CharField(verbose_name=_('Employee name'), max_length=30)
    position = models.CharField(verbose_name=_('Position in the organization'), max_length=30)
    text = models.TextField(verbose_name=_('Message from Employee'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Team'),
        verbose_name_plural = _('Teams')


class Contact(models.Model):
    """Contact with us"""
    name = models.CharField(verbose_name=_('Name contact user'), max_length=50)
    email = models.EmailField(verbose_name=_('Email in form'))
    subject = models.CharField(verbose_name=_('Subject in form'), max_length=50)
    message = models.TextField(verbose_name=_('Message from user'), max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact'),
        verbose_name_plural = _('Contacts')


class Card(models.Model):
    """Card in about us section"""
    img = models.FileField(
        verbose_name=_('Svg image'),
        upload_to='card',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['svg'])]
    )
    title = models.CharField(verbose_name=_('Card name'), max_length=30)
    text = models.TextField(verbose_name=_('Card text'), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Card'),
        verbose_name_plural = _('Cards')
