from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Kitten(models.Model):
    color = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(1),
                                          MaxValueValidator(360)])
    description = models.TextField()
    breed = models.ForeignKey('Breed',
                              on_delete=models.PROTECT,
                              related_name='kittens')

    def __str__(self):
        return f'kitten, color: {self.color}, age: {self.age} months'


class Breed(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'breed: {self.title}'
