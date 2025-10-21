from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/places/', views.activity_places_api, name='activity_places_api'),
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
]
