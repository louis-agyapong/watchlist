from http import HTTPStatus

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response

from core.watchlist.api.serializers import MovieSeriazer
from core.watchlist.models import Movie


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        try:
            movies = Movie.objects.all()
        except Movie.DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)
        serializer = MovieSeriazer(movies, many=True)
        return Response(data=serializer.data)

    if request.method == "POST":
        serializer = MovieSeriazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    """
    Retrieve, update or delete
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=HTTPStatus.NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSeriazer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MovieSeriazer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=HTTPStatus.NO_CONTENT)


class MovieListAPIView(APIView):
    def get(self, request):
        movies = get_list_or_404(Movie)
        serializer = MovieSeriazer(movies, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = MovieSeriazer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSeriazer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie)
        serializer = MovieSeriazer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=HTTPStatus.NO_CONTENT)