from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meter_api import views

router = DefaultRouter()
router.register('meter', views.MeterViewset)
router.register('metric', views.MeterMetricsViewset)
#router.register('max/<str:code>', views.MaxMeasureViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('metric/max/<str:code>', views.MaxMetricsViewset.as_view({'get':'list'})),
    path('metric/min/<str:code>', views.MinMetricsViewset.as_view({'get': 'list'})),
    path('metric/average/<str:code>', views.AverageMetricsViewset.as_view({'get': 'list'})),
    path('metric/total/<str:code>', views.TotalMetricsViewset.as_view({'get': 'list'})),

]