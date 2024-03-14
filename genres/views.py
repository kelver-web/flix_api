from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from genres.api.serializers import GenreSerializer

from .models import Genre

# from .permissions import GenrePermissionClass
from project.permissions import GlobalDefaultPermissions

# Create your views here.


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# class GenreRetrieveUpdateDestroyView(viewsets.ModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer


# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{"id": genre.id, "name": genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode("utf-8"))
#         new_genre = Genre(name=data["name"])
#         new_genre.save()
#         return JsonResponse(
#             {"id": new_genre.id, "name": new_genre.name},
#             status=201,
#         )


# @csrf_exempt
# def genre_detail_view(request, id):
#     genre  = get_object_or_404(Genre, id=id)

#     if request.method == 'GET':
#         data = {"id": genre.id, "name": genre.name}
#         return JsonResponse(data)

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode("utf-8"))
#         genre.name = data["name"]
#         genre.save()
#         return JsonResponse({"id": genre.id, "name": genre.name})

#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {"message": "Gênero deletado com sucesso."},
#             status=204,
#         )
