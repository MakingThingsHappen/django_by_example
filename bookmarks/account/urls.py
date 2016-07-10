from django.conf.urls import url
from django.contrib.auth import views
from . import views as account_views

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^$', account_views.dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login, name='logout_then_login'),
]
