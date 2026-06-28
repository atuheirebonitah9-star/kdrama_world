
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Template views
    path('', views.home, name='home'),
    path('dramas/', views.drama_list, name='drama_list'),
    path('dramas/<int:drama_id>/', views.drama_detail, name='drama_detail'),
    path('profile/', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('dramas/<int:drama_id>/add-to-watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('dramas/<int:drama_id>/add-review/', views.add_review, name='add_review'),
    
    # API views - auth
    path('api/auth/register/', views.UserRegistrationView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API views - dramas
    path('api/dramas/', views.DramaListCreateView.as_view(), name='drama-list'),
    path('api/dramas/<int:pk>/', views.DramaDetailView.as_view(), name='drama-detail'),
]
