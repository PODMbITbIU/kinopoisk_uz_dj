from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("movies/", views.MovieListView.as_view()),
    path("movies/<int:pk>/", views.MovieDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("person/", views.PersonsListView.as_view()),
    path("person/<int:pk>/", views.PersonsDetailView.as_view()),
    path("ratings/", views.AddStarRatingView.as_view()),
]
