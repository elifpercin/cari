from django import template
from hesap.models import Ucret

register = template.Library()


@register.filter
def get_ucret(post):
    if post is not None:

            ucret = Ucret.objects.get(ders=post.ders)
            adet_ucret = ucret.ucret

            return adet_ucret


