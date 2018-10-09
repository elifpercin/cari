from django.conf.urls import url

from .views import post_list, post_detail, post_create, form_ornek, deneme ,post_delete,post_update,odeme_al

urlpatterns = [
    url(r'^$', view=post_list, name='post_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', view=post_detail, name='post_detail'),
    url(r'^create/$', view=post_create, name='post_create'),
    url(r'^update/(?P<pk>[0-9]+)/$', view=post_update, name='post_update'   ),
    url(r'^form/$', view=form_ornek),
    url(r'^deneme/$', view=deneme),
    url(r'^delete/(?P<pk>[0-9]+)/$', view=post_delete, name='post_delete'),
    url(r'^odeme_al/(?P<pk>[0-9]+)/$', view=odeme_al, name='odeme_al')


]