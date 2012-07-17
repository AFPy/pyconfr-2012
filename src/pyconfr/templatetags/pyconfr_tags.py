from django.template import Library


register = Library()


@register.inclusion_tag('tags/sponsor_infos.html')
def sponsor_infos(level, sponsors):
    return {
            'template': 'tags/sponsor_infos.html',
            'level': level,
            'sponsors': sponsors
            }
