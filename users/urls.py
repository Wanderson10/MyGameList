from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairView


urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/image/", views.UserImageView.as_view()),
    path("users/<int:user_id>",views.UserDetailView.as_view()),
    # path("users/login/",TokenObtainPairView.as_view()),
    path('users/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]