from django.db import models

from simracerindonesia.users.models import User
from simracerindonesia.utils.managers import DefaultSelectOrPrefetchManager
from simracerindonesia.utils.models import TimeStampedModel


def generate_race_car_picture_path(instance, filename):
    return 'race_cars/{}/{}/{}'.format(
        instance.car_model.manufacturer.name,
        instance.car_model.name,
        filename
    )


class CarManufacturer(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(TimeStampedModel):
    manufacturer = models.ForeignKey(CarManufacturer,
                                     on_delete=models.PROTECT,
                                     related_name='models')
    name = models.CharField(max_length=100)

    objects = DefaultSelectOrPrefetchManager(select_related=('manufacturer',))

    def __str__(self):
        return '{} {}'.format(self.manufacturer, self.name)


class RaceCar(TimeStampedModel):
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    picture = models.ImageField(
        null=True, blank=True, upload_to=generate_race_car_picture_path
    )
    name = models.CharField(max_length=50, help_text='With the mod name')

    objects = DefaultSelectOrPrefetchManager(select_related=('car_model',))

    def __str__(self):
        return '{} ({})'.format(self.name, self.car_model)


class Series(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Series'


class RaceWeekend(TimeStampedModel):
    date = models.DateField()

    practice_start = models.TimeField()
    qualify_start = models.TimeField()
    race_start = models.TimeField()

    series = models.ForeignKey(Series)

    def __str__(self):
        return '{} {}'.format(self.date, self.series)


class Result(TimeStampedModel):
    race_weekend = models.ForeignKey(RaceWeekend)
    position = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return '{} - {} - {}'.format(self.position, self.user,
                                     self.race_weekend)

    class Meta:
        unique_together = (('race_weekend', 'position', 'user'),)


class Registration(TimeStampedModel):
    user = models.ForeignKey(User)
    series = models.ForeignKey(Series)

    def __str__(self):
        return '{} - {}'.format(self.user, self.series)
