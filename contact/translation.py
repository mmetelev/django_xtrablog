from modeltranslation.translator import register, TranslationOptions
from .models import About, Team, Contact, Card


@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('image', 'location', 'phone_number', 'email_blog')


@register(Team)
class ActorTranslationOptions(TranslationOptions):
    fields = ('image', 'name', 'position')


@register(Contact)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'subject', 'message')


@register(Card)
class ActorTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
