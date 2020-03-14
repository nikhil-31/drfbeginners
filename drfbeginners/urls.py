from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from posts.views import PostDetailView, PostDestroyView, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/<pk>/', PostDetailView.as_view(), name='post-list'),
    path('api/posts/<pk>/delete/', PostDestroyView.as_view(), name='post-list'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('quickstart/', include('quickstart.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/posts/', PostView.as_view()),
    # path('api/posts/', PostMixinListView.as_view(), name='post-list'),
    # path('api/posts/', PostView.as_view(), name='post-list'),
    # path('api/posts/<int:pk>/', PostView.as_view(), name='post-detail'),
    # path('api/posts/', post_list, name='post-list'),
]
