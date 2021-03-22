from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.uploadfiles, name='upload' ),
    path('my-videos/', views.myvideos, name = 'myfiles'),
    path('', views.home, name = 'home'),
    path('like/', views.add_like, name = 'like'),
    path('add-watchlist/', views.add_to_watchlist, name = 'add-watchlist'),
]
