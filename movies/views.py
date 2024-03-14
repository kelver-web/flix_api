from django.db.models import Count, Avg
from rest_framework import viewsets, views, response, status
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from reviews.models import Review
from movies.api.serializers import MovieSerializer, MovieListDetailSerializer
from project.permissions import GlobalDefaultPermissions


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    # serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


# class MovieRetrieveUpdateDestroyView(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reveiws': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }, status=status.HTTP_200_OK
        )
