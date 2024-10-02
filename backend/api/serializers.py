from rest_framework import serializers

from kittens.models import Breed, Kitten


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'title')


class KittenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kitten
        fields = ('color', 'age', 'description', 'breed')


class ReadOnlyKittenSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Kitten
        fields = ('id', 'color', 'age', 'description', 'breed')
