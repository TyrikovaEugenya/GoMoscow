from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import ActivityPlace

USE_MOCK_DATA = True

def index(request):
    return render(request, "base.html", context=None)

def activity_places_api(request):
    if USE_MOCK_DATA:
        places = [
            {
                "id": 1,
                "name": "Парк Горького",
                "description": "Один из крупнейших парков Москвы. Здесь можно кататься на велосипедах, роликах, заниматься йогой и играть в настольный теннис.",
                "latitude": 55.7338,
                "longitude": 37.5889,
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Gorky_Park_Moscow_2022.jpg/800px-Gorky_Park_Moscow_2022.jpg"
            },
            {
                "id": 2,
                "name": "ВДНХ",
                "description": "Выставка достижений народного хозяйства — огромная территория с музеями, фонтанами, катком и зонами для спорта.",
                "latitude": 55.8277,
                "longitude": 37.6483,
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/VDNH_Moscow_2022.jpg/800px-VDNH_Moscow_2022.jpg"
            },
            {
                "id": 3,
                "name": "Скалодром 'Скит'",
                "description": "Популярный скалодром в центре Москвы для новичков и профессионалов.",
                "latitude": 55.7623,
                "longitude": 37.6252,
                "image_url": None
            }
        ]
    else:
        places = list(ActivityPlace.objects.values('id', 'name', 'description', 'latitude', 'longitude', 'image_url'))
    return JsonResponse(list(places), safe=False)