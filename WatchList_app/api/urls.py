from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StreamPlatformAV, WatchListAV, StreamPlatformDetailAV, WatchDetailAV, ReviewList
from .views import ReviewCreate, StreamPlatformVS, ReviewDetail

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='platform-details'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')

    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
