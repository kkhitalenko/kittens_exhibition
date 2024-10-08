from rest_framework import serializers

from kittens.models import Breed, Kitten, Rate


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'title')


class KittenSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(),
                                         slug_field='title')

    class Meta:
        model = Kitten
        fields = ('id', 'color', 'age', 'description', 'breed')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('value',)
