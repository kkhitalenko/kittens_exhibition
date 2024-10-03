from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BreedList, KittenViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'kittens', KittenViewSet, basename='kittens')

urlpatterns = [
    path('', include(router.urls)),
    path('breeds/', BreedList.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
