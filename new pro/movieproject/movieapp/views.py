from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RatingForm, ReviewForm, MovieForm
from .models import Movie, Review, Rating


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})


def add_movie(request):
    if request.method == 'POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movielist.html')  # Assuming you have a view named 'movie_list' to show the movies
    else:
        form=MovieForm()

    return render(request, 'add.html', {'form': form})





def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def register(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different one.")

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.save()

        # Log the user in after registration
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Registration successful. You are now logged in.")
        else:
            return HttpResponse("An error occurred while logging in after registration.")
    else:
        # Render the registration form
        return render(request, 'register.html')

# views.py


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def logout_user(request):
     logout(request)
     return redirect('/')

def movie_list(request):
    # Retrieve all movies from the database
    movies = Movie.objects.all()
    return render(request, 'movielist.html', {'movie_list': movies})


def user_profile(request):
    # Pass the logged-in user object to the template
    return render(request, 'user.html', {'user': request.user})


def search(request):
    query = request.GET.get('q', '')
    movie_list = Movie.objects.filter(name__icontains=query)  # Adjust the filter as needed
    context = {
        'query': query,
        'movie_list': movie_list,
    }
    return render(request, 'search.html', context)





def movie_reviews(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie_reviews.html', {'movie': movie, 'reviews': reviews})

def movie_ratings(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    return render(request, 'movie_ratings.html', {'movie': movie, 'ratings': ratings})

def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movieapp:detail', movie_id=movie_id)  # Correct redirect
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form, 'movie': movie})



def create_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.movie = movie
            rating.save()
            return redirect('movieapp:detail', movie_id=movie_id)  # Redirect to movie detail page after rating creation
    else:
        form = RatingForm()
    return render(request, 'create_rating.html', {'form': form, 'movie': movie})


