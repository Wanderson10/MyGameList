
from .serializers import ReviewSeializers
from .models import Review
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import ipdb
class ReviewViews(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticated]
    serializer_class = ReviewSeializers

    queryset = Review.objects.all()
    def perform_create(self, serializer):
      
        serializer.save(  user = self.request.user, )
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSeializers
  
    queryset = Review.objects.all()

    lookup_url_kwarg = 'review_id'


class ReviewBulkDeleteView(generics.DestroyAPIView):
   
    queryset = Review.objects.all()
    serializer_class = ReviewSeializers
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=204)