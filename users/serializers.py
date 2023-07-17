from rest_framework import serializers
from .models import User,UserImage
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class userSerializer(serializers.ModelSerializer):
     

   class Meta:
        model = User
        fields = ["id","username","email","date_joined","phone_number","date_joined","password","is_superuser"]
        extra_kwargs ={'password' : {'write_only':True}}
   def create(self, validated_data: dict) -> User:
        print(validated_data)
        
            
        return User.objects.create_user(**validated_data)
   def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
   
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Inclua os dados do usuário no retorno
        user = self.user
     
        data['user'] = userSerializer(user).data
        # Adicione outros campos que você deseja retornar

        return data
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserImage
        fields = ["id",'user_image',"user","is_superuser"]
        read_only_fields =["id","user","is_superuser"]