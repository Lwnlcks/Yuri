from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
]