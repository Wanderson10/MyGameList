
from rest_framework import generics
from .serializers import userSerializer,ImageSerializer
from .models import User, UserImage
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class LoginView(generics.CreateAPIView):
    ...

class UserView(generics.ListCreateAPIView):
    
    serializer_class = userSerializer
  
    queryset = User.objects.all()
    
    ...

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = userSerializer
  
    queryset = User.objects.all()
    
    lookup_url_kwarg = 'user_id'

class UserImageView(generics.CreateAPIView):
     authentication_classes=[JWTAuthentication]
     permission_classes =[IsAuthenticated]
     serializer_class = ImageSerializer

     queryset = UserImage.objects.all()
     def perform_create(self, serializer):
      
        serializer.save(  user = self.request.user, )