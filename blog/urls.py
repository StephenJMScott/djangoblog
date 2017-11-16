from django.conf.urls import url
from blog.views import get_posts

urlpatterns = [
    
    url(r'^posts/', get_posts),
    
    ]
