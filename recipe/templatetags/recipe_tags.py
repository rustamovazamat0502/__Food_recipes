from django import template
from recipe.models import Category
from django.db.models import Count
from django import template

register = template.Library()


@register.simple_tag()
def get_all_categories():
    categories = Category.objects.annotate(Count("recipe"))
    return categories


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
