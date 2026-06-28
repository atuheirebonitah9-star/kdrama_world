
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Drama, UserPreference, Watchlist, Review, RecommendationLog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DramaSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Register view
class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Drama views
class DramaListCreateView(generics.ListCreateAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DramaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Original template views for backward compatibility (optional)
def home(request):
    dramas = Drama.objects.all()
    return render(request, 'series/home.html', {'dramas': dramas})

def drama_list(request):
    dramas = Drama.objects.all()
    return render(request, 'series/drama_list.html', {'dramas': dramas})

def drama_detail(request, drama_id):
    drama = get_object_or_404(Drama, id=drama_id)
    reviews = Review.objects.filter(drama=drama)
    return render(request, 'series/drama_detail.html', {'drama': drama, 'reviews': reviews})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'series/profile.html', {'profile': profile})

@login_required
def watchlist(request):
    watchlist_items = Watchlist.objects.filter(user=request.user)
    return render(request, 'series/watchlist.html', {'watchlist_items': watchlist_items})

@login_required
def add_to_watchlist(request, drama_id):
    drama = get_object_or_404(Drama, id=drama_id)
    Watchlist.objects.get_or_create(
        user=request.user,
        drama=drama,
        defaults={'status': 'Plan to Watch'}
    )
    return redirect('drama_detail', drama_id=drama_id)

@login_required
def add_review(request, drama_id):
    if request.method == 'POST':
        drama = get_object_or_404(Drama, id=drama_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(
            user=request.user,
            drama=drama,
            rating=rating,
            comment=comment
        )
        return redirect('drama_detail', drama_id=drama_id)

@csrf_exempt
def api_drama_list(request):
    if request.method == 'GET':
        dramas = Drama.objects.all().values()
        return JsonResponse(list(dramas), safe=False)

@csrf_exempt
def api_drama_detail(request, drama_id):
    try:
        drama = Drama.objects.get(id=drama_id)
        return JsonResponse({
            'id': drama.id,
            'title': drama.title,
            'genre': drama.genre,
            'episodes': drama.episodes,
            'release_year': drama.release_year,
            'rating': drama.rating,
            'description': drama.description
        })
    except Drama.DoesNotExist:
        return JsonResponse({'error': 'Drama not found'}, status=404)
