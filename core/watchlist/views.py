from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse, Http404


def movie_list(request) -> JsonResponse:
    movies = Movie.objects.values("title", "active")
    data = {"results": list(movies)}
    return JsonResponse(data)


def movie_detail(request, pk) -> JsonResponse:
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    data = {
        "results": {
            "title": movie.title,
            "plot": movie.plot,
            "active": movie.active,
        }
    }
    return JsonResponse(data)
