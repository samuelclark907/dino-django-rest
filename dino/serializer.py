from rest_framework import serializers
from .models import Dino

class DinoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creator', 'name', 'description', 'created_at')
        model = Dino