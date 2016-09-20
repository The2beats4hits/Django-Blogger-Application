from django.conf.urls import url,include
from .views import PostsListView, PostDetailView, OwnerPostsListView
from . import views
urlpatterns = [
url(r'^$', PostsListView.as_view(), name='list'),
url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
url(r'^comments/', include('django_comments.urls')),
url(r'^post_new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
url(r'^my_posts/$', OwnerPostsListView.as_view(), name='my_posts'),
]
