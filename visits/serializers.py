# visits/serializers.py
from rest_framework import serializers
from .models import RetailPoint, Visit

class RetailPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailPoint
        fields = ['id', 'name']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'datetime']
