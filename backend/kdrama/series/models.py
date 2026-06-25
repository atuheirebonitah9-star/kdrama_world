from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Drama(models.Model):
    GENRE_CHOICES = [
        ('Romance', 'Romance'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Historical', 'Historical'),
        ('Fantasy', 'Fantasy'),
        ('Action', 'Action'),
        ('Mystery', 'Mystery'),
    ]

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    episodes = models.IntegerField()
    release_year = models.IntegerField()
    rating = models.FloatField(default=0.0)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title
    
class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genres = models.CharField(max_length=255)
    favorite_actor = models.CharField(max_length=255, blank=True, null=True)
    mood_preference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
class Watchlist(models.Model):
    STATUS_CHOICES = [
        ('Watching', 'Watching'),
        ('Completed', 'Completed'),
        ('Plan to Watch', 'Plan to Watch'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('user', 'drama')

    def __str__(self):
        return f"{self.user.username} - {self.drama.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.drama.title}"
    
class RecommendationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.drama.title}"
    

