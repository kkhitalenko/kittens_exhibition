from rest_framework import generics, viewsets

from api.serializers import (BreedSerializer, KittenSerializer,
                             ReadOnlyKittenSerializer)
from kittens.models import Breed, Kitten


class BreedList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadOnlyKittenSerializer
        return KittenSerializer
