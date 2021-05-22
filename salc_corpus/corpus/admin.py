from django.contrib import admin
from . import models
from .models import Corpus



class CorpusAdmin(admin.ModelAdmin):
    list_display = ("language", "task", "utterance")

admin.site.register(Corpus, CorpusAdmin)
