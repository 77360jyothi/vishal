from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()  # You might want to remove this field since you now have `release_date`

    actors = models.CharField(max_length=500)  # Adjust the length as needed
    trailer_link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.name}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating scale from 1 to 5

    def __str__(self):
        return f"{self.user.username}'s rating ({self.rating}) for {self.movie.name}"