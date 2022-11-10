from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie/", include("core.watchlist.urls")),
    path("api/movie/", include("core.watchlist.api.urls"))
]
