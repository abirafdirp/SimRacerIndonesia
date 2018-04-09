from django.contrib import admin
from reversion.admin import VersionAdmin

from . import models
from simracerindonesia.utils.admin import TimeStampedModelAdminMixin


@admin.register(models.CarManufacturer)
class CarManufacturerAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass


@admin.register(models.CarModel)
class CarModelAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass


@admin.register(models.RaceCar)
class RaceCarAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass


@admin.register(models.Series)
class SeriesAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass


@admin.register(models.RaceWeekend)
class RaceWeekendAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass


@admin.register(models.RacingSimulator)
class RacingSimulatorAdmin(TimeStampedModelAdminMixin, VersionAdmin):
    pass
