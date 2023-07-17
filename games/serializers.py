from rest_framework import serializers
from .models import Game
from reviews.models import Review
from genders.models import Gender
from genders.serializers import GendersSerializer
import ipdb
from reviews.serializers import ReviewSeializers

class GameSerializer(serializers.ModelSerializer):
    users_avaliations = serializers.SerializerMethodField(method_name="avaliations")
    
    number_of_reviews = serializers.SerializerMethodField(method_name="numbers")
    genders = GendersSerializer(many=True)

    class Meta:
        model = Game
        fields = ["id", "name_game", "description", "game_logo",
                  "made_by", "users_avaliations",'number_of_reviews', "genders",]
        read_only_fields = ["id", "users_avaliations",'number_of_reviews','users_avaliations',]
    def avaliations(self,obj:Review):
        reviews = obj.reviews.all()
        game_id = obj.id
        number_avaliations = 0
        result= 0
        if reviews:
         my_data = ReviewSeializers(reviews, many=True).data
         print(my_data)
            
         for i in my_data:
             if i["game"] == game_id:
                number_avaliations = number_avaliations+ 1
                result = result + i['rate']
         return result / number_avaliations
        else :
            return 'not players avaliations yet'
    def numbers(self,obj:Review):
            reviews = obj.reviews.all()
            number_avaliations = 0 
            if reviews:
                 for i in reviews:
                    number_avaliations = number_avaliations+ 1
            
            return number_avaliations

    def create(self, validated_data):
       
        gender_data = validated_data.pop('genders')
        
        game = Game.objects.create(**validated_data)
        for i in  gender_data:
            print(i)
            gender, _ = Gender.objects.get_or_create(**i)
            game.genders.add(gender)
        game.save()
        return game
    def update(self, instance:Game, validated_data):
       
        gender_data = validated_data.pop('genders',None)

        if gender_data:
            for i in gender_data:
              gender, _ = Gender.objects.get_or_create(**i)
              instance.genders.clear()
              instance.genders.add(gender)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
       
