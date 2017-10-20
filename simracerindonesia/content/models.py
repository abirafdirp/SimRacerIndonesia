from django.db import models

from simracerindonesia.utils.models import TimeStampedModel


class HomePage(TimeStampedModel):
    main_image = models.ImageField()


class HomePageCarouselImage(TimeStampedModel):
    file = models.ImageField()
    home_page = models.ForeignKey(HomePage, related_name='carousel_images',
                                  on_delete=models.CASCADE)