from django import forms
from .models import Review, Rating, Movie


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']




class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc', 'year', 'actors', 'trailer_link', 'img']
