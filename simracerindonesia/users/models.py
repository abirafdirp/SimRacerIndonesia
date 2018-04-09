from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from simracerindonesia.utils.models import TimeStampedModel


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username


class UserProfile(TimeStampedModel):
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )
    SIMRACING_EXPERIENCE_CHOICES = (
        ('', ''),
        ('Less than 1 year', 'Less than 1 year'),
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('4 years', '4 years'),
        ('5 years', '5 years'),
        ('More than 5 years', 'More than 5 years'),
    )

    user = models.OneToOneField(User, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                              blank=True, null=True)
    birth_year = models.DateField(blank=True, null=True)
    racing_simulators = models.ManyToManyField(
        'core.RacingSimulator', blank=True, related_name='racing_simulators'
    )
    simracing_experience = models.CharField(
        choices=SIMRACING_EXPERIENCE_CHOICES, blank=True,
        max_length=20, default=''
    )
    real_life_racing_experience = models.BooleanField(default=False)
    highest_simracing_achievement = models.TextField(blank=True, default='')
    favourite_cars = models.TextField(blank=True, default='')
    hardware = models.TextField(blank=True, default='')

    city = models.ForeignKey('cities_light.City', blank=True, null=True)
    # if city does not match use country as it likely not be typo/not matched
    country = models.ForeignKey('cities_light.Country', blank=True, null=True)

    city_freetext = models.CharField(max_length=100, blank=True, null=True)
    country_freetext = models.CharField(max_length=100, blank=True, null=True)
