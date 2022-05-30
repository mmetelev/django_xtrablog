from django import template
from blog.models import Category

register = template.Library()


@register.simple_tag()
def get_all_category():
    return Category.objects.all()
