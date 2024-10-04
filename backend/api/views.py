from django.db import IntegrityError
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.permissions import IsOwnerOrReadOnly
from api.serializers import BreedSerializer, KittenSerializer, RateSerializer
from kittens.models import Breed, Kitten, Rate, User


class BreedList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    serializer_class = KittenSerializer
    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(methods=['post'], detail=True,
            permission_classes=[permissions.IsAuthenticated])
    def rate(self, request, pk):
        serializer = RateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        value = serializer.validated_data['value']
        kitten = self.get_object()
        user = User.objects.get(id=request.user.id)

        try:
            Rate.objects.create(value=value, kitten=kitten, user=user)
        except IntegrityError:
            return Response({'errors': 'Вы уже оценили этого котика'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        breed = self.request.query_params.get('breed')
        if breed is not None:
            return Kitten.objects.filter(breed__title=breed)
        return Kitten.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
