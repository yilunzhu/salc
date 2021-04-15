from django.urls import path
from corpus import views

urlpatterns = [
    path('index/', views.corpus_index, name='corpus_index'),
]