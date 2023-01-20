from django.db import models


# Create your models here.
class Meter(models.Model):
    """Meter object model"""
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16)


class MeterMetrics(models.Model):
    """Handling consumption metrics from the meter"""
    consumption_meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='consumption')
    received_date = models.DateTimeField(auto_now_add=True)
    # Preferiría usar ArrayField del modulo postgres, pero ya que usamos SQLite usaré una solución que se adecue
    kwh_consumption = models.IntegerField()
