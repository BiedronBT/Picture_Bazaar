from django import template

register = template.Library()

@register.filter(name='onlyfirst')
def onlyfirst(strng):
    x = strng.split(',')
    return x[0]