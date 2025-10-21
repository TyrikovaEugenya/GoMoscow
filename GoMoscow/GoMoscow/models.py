from django.db import models

class ActivityPlace(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    image_url = models.URLField("URL изображения", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name