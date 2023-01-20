from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db.models import Avg, Min, Max, Sum, Aggregate
from rest_framework import viewsets, generics
from rest_framework import filters
from rest_framework.response import Response

from meter_api import serializers
from meter_api import models


# Create your views here.

class MeterViewset(viewsets.ModelViewSet):
    """Handles creating, reading deleting and updating Meters"""
    serializer_class = serializers.MeterSerializer
    queryset = models.Meter.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'code')


class MeterMetricsViewset(viewsets.ModelViewSet):
    """Handles creating, reading, deleting and updating measurements from a meter"""
    serializer_class = serializers.MeterMetricsSerializer
    queryset = models.MeterMetrics.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('consumption_meter__code', 'consumption_meter__id')


class MaxMetricsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MeterSerializer

    def list(self, request, *args, **kwargs):
        code = self.kwargs['code']
        queryset = models.Meter.objects.filter(code=code)
        max_consumption = queryset[0].consumption.aggregate(Max('kwh_consumption'))
        return Response(max_consumption)


class MinMetricsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MeterSerializer

    def list(self, request, *args, **kwargs):
        code = self.kwargs['code']
        queryset = models.Meter.objects.filter(code=code)
        min_consumption = queryset[0].consumption.aggregate(Min('kwh_consumption'))
        return Response(min_consumption)


class AverageMetricsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MeterSerializer

    def list(self, request, *args, **kwargs):
        code = self.kwargs['code']
        queryset = models.Meter.objects.filter(code=code)
        average_consumption = queryset[0].consumption.aggregate(Avg('kwh_consumption'))
        return Response(average_consumption)


class TotalMetricsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MeterSerializer

    def list(self, request, *args, **kwargs):
        code = self.kwargs['code']
        queryset = models.Meter.objects.filter(code=code)
        total_consumption = queryset[0].consumption.aggregate(Sum('kwh_consumption'))
        return Response(total_consumption)


