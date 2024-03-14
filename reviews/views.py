from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from reviews.api.serializers import ReviewSerializer

from reviews.models import Review

from project.permissions import GlobalDefaultPermissions


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class ReviewRetrieveUpdateDestroyView(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
