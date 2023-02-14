from django import template
from pages.models import Page

#registrando el template en la libreria de templates
register=template.Library()

@register.simple_tag #convertir la funcon en un template tag
def get_page_list():
    pages=Page.objects.all()
    return pages