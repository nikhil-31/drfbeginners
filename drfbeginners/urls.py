from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from posts.views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', PostView.as_view(), name='post-list'),
    path('quickstart/', include('quickstart.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
