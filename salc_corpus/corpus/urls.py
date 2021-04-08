from django.urls import path
from corpus import views

urlpatterns = [
    path('index/', views.index, name='corpus_index'),
]