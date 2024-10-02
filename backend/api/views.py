from rest_framework import generics, viewsets

from api.serializers import BreedSerializer, KittenSerializer
from kittens.models import Breed, Kitten


class BreedList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    serializer_class = KittenSerializer

    def get_queryset(self):
        breed = self.request.query_params.get('breed')
        if breed is not None:
            return Kitten.objects.filter(breed__title=breed)
        return Kitten.objects.all()
