from .models import Corpus
import django_filters
from django import forms
from django.contrib.auth.models import User

class CorpusFilter(django_filters.FilterSet):

    language = django_filters.CharFilter(
        lookup_expr='exact',

        widget=forms.TextInput(attrs={'class': 'form-control'}))

    task = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    utterance = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Corpus
        fields = ['language', 'task', 'utterance' ]


