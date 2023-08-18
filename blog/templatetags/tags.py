from django import template

register = template.Library()


@register.simple_tag
def mediapath(path):
    return '/media/' + str(path)
