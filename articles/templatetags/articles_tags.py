from django import template
from django.template import Context, Template


register = template.Library()


@register.simple_tag(takes_context=True)
def render_descriprion(context, html):
    template = Template(html)
    new_html = template.render(context)
    return new_html
