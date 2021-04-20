from django.contrib import admin
from . import models
from .models import Corpus

class CorpusAdmin(admin.ModelAdmin):
    list_display = ("sample", "sopi","sopib", "pvc","language", "task", "utterance",)

admin.site.register(models.Corpus)
