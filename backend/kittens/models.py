from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


User = get_user_model()


class Kitten(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='kittens')
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


class Rate(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    kitten = models.ForeignKey(Kitten,
                               on_delete=models.CASCADE,
                               related_name='rates')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='rates')

    class Meta:
        constraints = [models.UniqueConstraint('kitten', 'user',
                                               name='unique_user_kitten_rate')]
