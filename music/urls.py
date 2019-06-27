from django.urls import path
from . import views


urlpatterns = [
     path('api/album/', views.AlbumListCreate.as_view() ),
    ]
