from rest_framework import serializers;
from .models import Review
from users.models import User
from games.models import Game

from users.serializers import userSerializer
from django.db import IntegrityError


class ReviewSeializers(serializers.ModelSerializer):
    
    review_made_by = serializers.SerializerMethodField()
    class Meta:
      model= Review
      fields=["id","review","user","game","rate",'review_made_by']
      read_only_fields = ["id", "user"]

    def create(self, validated_data):
    
        try:
            review = Review.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError( "You have already done a review for this game. you can edit or delete it or make review another  game ")

        return review
    def get_review_made_by(self,obj:Review):
        return obj.user.username
    
    
    
    