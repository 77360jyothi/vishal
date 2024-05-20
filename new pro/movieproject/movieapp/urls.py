
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [


    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('credentials/register', views.register, name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('movielist/', views.movie_list, name='movie_list'),
    path('user/', views.user_profile, name='user_profile'),
    path('search/', views.search, name='search'),
    path('movie/<int:movie_id>/reviews/', views.movie_reviews, name='movie_reviews'),
    path('movie/<int:movie_id>/ratings/', views.movie_ratings, name='movie_ratings'),
    path('movie/<int:movie_id>/review/', views.create_review, name='create_review'),
    path('movie/<int:movie_id>/rating/', views.create_rating, name='create_rating'),


]






