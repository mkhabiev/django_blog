from django.urls import path
from .views import add_post, PostsView, PostDetailView

urlpatterns = [
    path('posts', PostsView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('add-post/', add_post)
]