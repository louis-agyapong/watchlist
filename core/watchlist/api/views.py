from http import HTTPStatus

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response

from core.watchlist.api.serializers import MovieModelSerializer, MovieSeriazer, StreamingPlatformMS
from core.watchlist.models import Movie, StreamingPlatform


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
        serializer = MovieModelSerializer(movies, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieModelSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=HTTPStatus.NO_CONTENT)


class PlafformAPIView(APIView):
    def get(self, request):
        streaming_platforms = get_list_or_404(StreamingPlatform)
        serializer = StreamingPlatformMS(streaming_platforms, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = StreamingPlatformMS(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

class PlatformDetailAPIView(APIView):
    def get(self, request, pk):
        streaming_platform = get_object_or_404(StreamingPlatform, pk=pk)
        serializer = StreamingPlatformMS(streaming_platform)
        return Response(serializer.data)

    def put(self, request, pk):
        streaming_platform = get_object_or_404(StreamingPlatform, pk=pk)
        serializer = StreamingPlatformMS(streaming_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        streaming_platform = get_object_or_404(StreamingPlatform, pk=pk)
        streaming_platform.delete()
        return Response(status=HTTPStatus.NO_CONTENT)
