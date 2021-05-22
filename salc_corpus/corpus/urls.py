from django.urls import path
from corpus import views
from django.conf.urls import url
from .views import HomePageView,SearchResultsView,SearchlangView,SearchtaskView

from django.conf.urls import url #new


urlpatterns = [

    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_lang/', SearchlangView.as_view(), name='search_lang_results'),
    path('search_task/', SearchtaskView.as_view(), name='search_task_results'),
    path('', HomePageView.as_view(), name='home'),

]
