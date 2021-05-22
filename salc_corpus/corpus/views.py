from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Corpus
from django.db.models import Q
from .forms import CorpusFilter




class HomePageView(TemplateView):
    template_name = 'corpus_index.html'


class SearchResultsView(ListView):
    model = Corpus
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Corpus.objects.filter(
            Q(utterance__icontains=query)
        )
        return object_list


class SearchlangView(ListView):
    model = Corpus
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Corpus.objects.filter(
            Q(language__exact=query)
        )
        return object_list

class SearchtaskView(ListView):
    model = Corpus
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Corpus.objects.filter(
            Q(task__icontains=query)
        )
        return object_list
