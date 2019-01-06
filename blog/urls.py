

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^testing_JQuery/', views.testing_JQuery, name=
    'testing_JQuery'),
    url(r'^test_JQuery2/', views.test_JQuery2, name=
    'test_JQuery2'),
    url(r'^learn_css/', views.learn_css, name=
    'learn_css'),
    url(r'^practice_CSS2/', views.practice_CSS2, name='practice_CSS2'),
]
