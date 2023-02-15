from django.urls import path, include
from applications.post.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('comments', CommentsViewSet, basename='comment')
router.register('comment', CommentModeViewSet)
router.register('', PostModelViewSet)

urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIView.as_view()),
    # path('update/<int:pk>/', PostUpdateAPIView.as_view()),
    # path('delete/<int:pk>/', PostDeleteAPIView.as_view()),
    # path('detail/<int:pk>/', PostDetailAPIView.as_view()),
    path('', include(router.urls)),
    # path('posts/', PostlistCreateAPIView.as_view()),
    # path('<int:pk>/', PostDetailDeleteUpdateAPIView.as_view()),
    path('add/image/', CreateImageAPIView.as_view()),
    # path('comments/', CommentsViewSet.as_view({'get': 'list'}))
]
