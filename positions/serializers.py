from .models import Position

from rest_framework import serializers


class PositionSerializer(serializers.ModelSerializer):
    is_filled = serializers.BooleanField(read_only=True)

    class Meta:
        model = Position
        fields = '__all__'