from django.urls import path

from .views import (
    MovieDetailAPIView,
    MovieListAPIView,
    PlafformAPIView,
    PlatformDetailAPIView,
)

urlpatterns = [
    path("list/", MovieListAPIView.as_view(), name="movie_list"),
    path("<int:pk>/", MovieDetailAPIView.as_view(), name="movie_detail"),
    path("platform/list/", PlafformAPIView.as_view(), name="platform_list"),
    path("platform/<int:pk>/", PlatformDetailAPIView.as_view(), name="platform_detail"),
]
 