from django.contrib import admin

from kittens.models import Breed, Kitten


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'color', 'age', 'description', 'breed']
    list_filter = ['breed']

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
