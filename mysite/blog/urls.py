from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{2})/'
        r'(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

]
