from django.contrib import admin
from django.urls import path, include

from posts.views import OwnerDetailView, CommentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('posts.urls')),
    # path('api/posts/<pk>/', PostDetailView.as_view(), name='post-list'),
    # path('api/posts/<pk>/delete/', PostDestroyView.as_view(), name='post-list'),
    # path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/owner/<pk>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('api/comment/<pk>/', CommentDetailView.as_view(), name='comment-detail'),
    # path('quickstart/', include('quickstart.urls')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/posts/', PostView.as_view()),
    # path('api/posts/', PostMixinListView.as_view(), name='post-list'),
    # path('api/posts/', PostView.as_view(), name='post-list'),
    # path('api/posts/<int:pk>/', PostView.as_view(), name='post-detail'),
    # path('api/posts/', post_list, name='post-list'),
]
