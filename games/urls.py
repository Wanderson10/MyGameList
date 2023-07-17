from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("games/", views.gameViews.as_view()),
    path("games/<int:game_id>",views.gameDetailView.as_view()),
    path('games/delete-all/',views.GameBulkDeleteView.as_view(), name='delete-all-Games'),
]