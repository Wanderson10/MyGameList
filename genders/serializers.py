from rest_framework import serializers
from .models import Gender

class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ["id","name","created_at"]