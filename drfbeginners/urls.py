from django.contrib import admin
from django.urls import path, include

from posts.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/posts/', PostView.as_view(), name='post-list'),
    path('quickstart/', include('quickstart.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/posts/', post_list, name='post-list'),
    path('api/posts/<int:pk>', post_detail, name='post-detail')
]
