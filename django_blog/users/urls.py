from django.urls import path
from .views import ProfileView, ProfileDetailView, add_profile

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view()),
    path('add-profile/', add_profile),
]