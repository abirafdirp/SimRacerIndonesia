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

    user = models.OneToOneField(User, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_year = models.DateField()
    simracing_experience = models.IntegerField()
    real_life_racing_experience = models.BooleanField()
    highest_simracing_achievement = models.TextField()
