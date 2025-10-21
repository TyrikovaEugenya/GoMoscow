from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/places/', views.activity_places_api, name='activity_places_api'),
]