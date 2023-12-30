from django.urls import path
from .views import PostListCreateView, PostRetriveUpdateDestroyView, StudentListCreateView, StudentDetailView


urlpatterns = [
    path("tasks", PostListCreateView.as_view()),
    path("tasks/<int:id>", PostRetriveUpdateDestroyView.as_view()),

    path("students", StudentListCreateView.as_view()),
    path("students/<int:pk>", StudentDetailView.as_view()),
]