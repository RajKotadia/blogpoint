from django.urls import path
from .views import PostDetailView
from . import views


urlpatterns = [
    path('',  views.home, name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about',  views.about, name='about'),
]
