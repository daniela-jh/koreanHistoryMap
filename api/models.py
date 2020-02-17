from django.conf import settings
from django.db import models


class Content(models.Model):
    locationName = models.CharField(max_length=20)
    locationText1 = models.CharField(max_length=80)
    locationText2 = models.CharField(max_length=80)
    locationText3 = models.CharField(max_length=80)
    locationText4 = models.CharField(max_length=80)
    locLat = models.DecimalField(max_digits=12, decimal_places=9, default=None)
    locLng = models.DecimalField(max_digits=12, decimal_places=9, default=None)

    def contentSave(self):
        self.save()

    def __str__(self):
        return self.locationName