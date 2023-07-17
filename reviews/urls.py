from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("reviews/", views.ReviewViews.as_view()),
    path("reviews/<int:review_id>",views.ReviewDetailView.as_view()),
    path('reviews/delete-all/',views.ReviewBulkDeleteView.as_view(), name='delete-all-reviews'),
]