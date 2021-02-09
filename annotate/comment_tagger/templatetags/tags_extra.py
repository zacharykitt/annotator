from django import template

register = template.Library()


def format_tag(value):
    if value.startswith('_'):
        return value[1:]
    return value


register.filter('format_tag', format_tag)
