from django.db import models
from django.urls import reverse


class PhotoModel(models.Model):
    photo = models.ImageField()

    def get_url(self):
        return reverse('view_photo', args=(self.id,))
