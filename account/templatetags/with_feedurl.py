from django import template
import uuid

register = template.Library()


@register.filter
def with_feedurl(subscribes, feedurl):
    id_value = uuid.uuid3(uuid.NAMESPACE_DNS, feedurl)
    return subscribes.filter(id=id_value).first()
