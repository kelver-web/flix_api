from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from actors.models import Actors
from actors.api.serializers import ActorsSerializer

from project.permissions import GlobalDefaultPermissions
# Create your views here.


class ActorsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


# class ActorsRetrieveUpdateDestroyView(viewsets.ModelViewSet):
#     queryset = Actors.objects.all()
#     serializer_class = ActorsSerializer
