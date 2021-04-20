from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Corpus
from django.db.models import Q 

# @login_required(login_url='login', redirect_field_name='corpus_index')
#def corpus_index(request):
    #if not request.user.is_authenticated:
        #return render(request, 'login/login.html')
    #else:
        #return render(request, 'corpus/corpus_index.html')

class HomePageView(TemplateView):
    template_name = 'corpus_index.html'

class SearchResultsView(ListView):
    model = Corpus
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Corpus.objects.filter(
            Q(sample__icontains=query) | Q(utterance__icontains=query)| Q(task__icontains=query)
        )
        return object_list
