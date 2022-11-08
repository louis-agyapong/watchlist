from django.urls import path

from .views import movie_detail, movie_list, MovieDetailAPIView, MovieListAPIView

urlpatterns = [
    path("list/", MovieListAPIView.as_view(), name="movie_list"),
    path("<int:pk>/", MovieDetailAPIView.as_view(), name="movie_detail"),
]
 