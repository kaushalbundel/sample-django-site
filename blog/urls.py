from django.urls import path

from . import views
from .views import (
    BlogListView,BlogDetailView
)

urlpatterns=[
    path('', BlogListView.as_view(),name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('blog/<int:pk>/',BlogDetailView.as_view(),name='blog-detail'),


]