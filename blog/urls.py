from django.conf.urls import url
from blog.views import get_posts, viewpost, newpost, editpost

urlpatterns = [
    
    url(r'^posts/$', get_posts, name="posts"),
    url(r'^posts/(\d+)$', viewpost, name ="viewpost"),
    url(r'^posts/add', newpost, name="newpost"),
    url(r'^posts/(\d+)/edit$', editpost, name="editpost"),
    
    ]
