from django.contrib import admin
from meter_api import models
# Register your models here.

admin.site.register(models.Meter)
admin.site.register(models.MeterMetrics)