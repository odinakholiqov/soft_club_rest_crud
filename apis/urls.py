from django.urls import path
from .views import PostListCreateView, PostRetriveUpdateDestroyView

urlpatterns = [
    path("tasks", PostListCreateView.as_view()),
    path("tasks/<int:id>/", PostRetriveUpdateDestroyView.as_view())
]