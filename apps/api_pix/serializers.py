from rest_framework import serializers

from .models import Charge


class ChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        exclude = ['user',]
        extra_kwargs = {"txid": {"required": False}}
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        