from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login', redirect_field_name='corpus_index')
def corpus_index(request):
    if not request.user.is_authenticated:
        return render(request, 'login/login.html')
    else:
        return render(request, 'corpus/corpus_index.html')