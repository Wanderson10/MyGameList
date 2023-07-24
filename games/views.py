from django.shortcuts import render
from .serializers import GameSerializer
from .models import Game
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class gameViews(generics.ListCreateAPIView):
    
    serializer_class = GameSerializer
  
    queryset = Game.objects.all()


class gameDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]
    
    serializer_class = GameSerializer
  
    queryset = Game.objects.all()

    lookup_url_kwarg = 'game_id'
class GameBulkDeleteView(generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]  
    queryset =Game.objects.all()
    serializer_class =GameSerializer

    def delete(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=204)