import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    # https://python-markdown.github.io/extensions/
    extensions = ["footnotes", "fenced_code", "nl2br", "md_in_html"]
    return mark_safe(markdown.markdown(value, extensions=extensions))