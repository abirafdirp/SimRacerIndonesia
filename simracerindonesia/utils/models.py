from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        self.update_date = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
