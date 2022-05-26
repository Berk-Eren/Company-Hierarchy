import imp
from .models import Department
from positions.serializers import PositionSerializer

from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    has_positions = PositionSerializer(source="product_set", many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'