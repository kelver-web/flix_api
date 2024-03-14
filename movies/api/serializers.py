from django.db.models import Avg

from rest_framework import serializers

from movies.models import Movie
from actors.api.serializers import ActorsSerializer
from genres.api.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

        # reviews = obj.reviews.all()
        # list_reviews = []

        # if reviews:
        #     for review in reviews:
        #         list_reviews.append(review.stars)

        #     total = sum(list_reviews) / len(list_reviews)

        #     return round(total, 1)

        # return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento tem que ser maior que o ano de 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo deve ter no máximo 200 caracteres.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorsSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
