from rest_framework import serializers
from PropertyValuation.models import PropertyValuationModel


class PropertyValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValuationModel
        fields = [
            "id",
            "plot_price_per_meter_square",
            "apartment_price_per_meter_square",
            "city",
            "house_price_per_meter_square",
        ]
        
        
