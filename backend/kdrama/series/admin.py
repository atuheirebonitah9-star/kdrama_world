from django.contrib import admin
from .models import Profile, Drama, UserPreference, Watchlist, Review, RecommendationLog

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    list_filter = ['user']
    search_fields = ['user__username', 'bio']

@admin.register(Drama)
class DramaAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'episodes', 'release_year', 'rating']
    list_filter = ['genre', 'release_year']
    search_fields = ['title', 'description']

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'favorite_genres', 'favorite_actor']
    list_filter = ['favorite_genres']
    search_fields = ['user__username', 'favorite_genres', 'favorite_actor']

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'drama', 'status']
    list_filter = ['status', 'user']
    search_fields = ['user__username', 'drama__title']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'drama', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'user']
    search_fields = ['user__username', 'drama__title', 'comment']

@admin.register(RecommendationLog)
class RecommendationLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'drama', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'drama__title', 'reason']

