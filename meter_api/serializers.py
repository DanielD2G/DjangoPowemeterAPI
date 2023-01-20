from rest_framework import serializers

from meter_api import models


class MeterSerializer(serializers.ModelSerializer):
    """Serializes the meter object"""

    class Meta:
        model = models.Meter
        fields = ('name', 'code')

        def validate(self, validated_data):
            if 1111 < validated_data['code'] > 9999:
                raise serializers.ValidationError("Code should be 4 characters")
            return validated_data


class MeterMetricsSerializer(serializers.ModelSerializer):
    """Serializes the conpsumptions from the meter"""

    class Meta:
        model = models.MeterMetrics
        fields = ('consumption_meter', 'received_date', 'kwh_consumption')
        extra_kwargs = {
            'received_date': {'read_only': True}
        }


