from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dramas/', views.drama_list, name='drama_list'),
    path('dramas/<int:drama_id>/', views.drama_detail, name='drama_detail'),
    path('profile/', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('dramas/<int:drama_id>/add-to-watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('dramas/<int:drama_id>/add-review/', views.add_review, name='add_review'),
    path('api/dramas/', views.api_drama_list, name='api_drama_list'),
    path('api/dramas/<int:drama_id>/', views.api_drama_detail, name='api_drama_detail'),
]
