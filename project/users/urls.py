from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.ListCreateUsersView.as_view()),
    path('users/<user_id>/', views.ListUpdateDeleteUserByID.as_view()),
]