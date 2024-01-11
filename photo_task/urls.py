from django.urls import path, include
from .views import ImagesList, ImagesCreate

urlpatterns = [
    path('images/', ImagesList.as_view(), name='image-list'),
    path('images/random/', ImagesCreate.as_view(), name='image-list'),
]
