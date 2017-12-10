from django.db import models

from simracerindonesia.utils.models import TimeStampedModel


def generate_race_car_picture_path(instance, filename):
    return 'race_cars/{}/{}/{}'.format(
        instance.car_model.manufacturer.name,
        instance.car_model.name,
        filename
    )


class CarManufacturer(TimeStampedModel):
    name = models.CharField(max_length=100)


class CarModel(TimeStampedModel):
    manufacturer = models.ForeignKey(CarManufacturer,
                                     on_delete=models.PROTECT,
                                     related_name='models')
    name = models.CharField(max_length=100)


class RaceCar(TimeStampedModel):
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    picture = models.ImageField(
        null=True, blank=True, upload_to=generate_race_car_picture_path
    )


class Series(TimeStampedModel):
    name = models.CharField(max_length=100)


class RaceWeekend(TimeStampedModel):
    practice_start = models.TimeField()
    qualify_start = models.TimeField()
    race_start = models.TimeField()


class Race(TimeStampedModel):
    qualify_length = models.IntegerField(help_text='In minutes')
