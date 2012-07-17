import random
from django.template import Library


register = Library()


@register.inclusion_tag('tags/sponsor_infos.html')
def sponsor_infos(level, sponsors):
    return {
            'template': 'tags/sponsor_infos.html',
            'level': level,
            'sponsors': sponsors
            }


@register.filter
def shuffle(arg):
    """
    shuffle filter for templates.
    http://stackoverflow.com/questions/7162629/django-shuffle-in-templates
    """
    tmp = arg[:]
    random.shuffle(tmp)
    return tmp
