from django.db import models
from django import forms

class Corpus(models.Model):
    
    sample = models.CharField(max_length=30)
    gender = models.IntegerField()
    age = models.IntegerField()
    sopi = models.FloatField()
    sopib = models.FloatField()
    duration = models.IntegerField()
    program = models.IntegerField()
    pvc = models.IntegerField()
    language = models.TextField(max_length=30)
    task = models.CharField(max_length=100)
    utterance = models.CharField(max_length=100000)

    class Meta:
        app_label = 'corpus'
