from django.db import models


class Corpus(models.Model):
    sample = models.CharField(max_length=30)
    gender = models.IntegerField()
    age = models.IntegerField()
    sopi = models.FloatField()
    sopib = models.FloatField()
    duration = models.IntegerField()
    program = models.IntegerField()
    pvc = models.IntegerField()
    language = models.CharField(max_length=30)
    task = models.CharField(max_length=30)
    utterance = models.CharField(max_length=100)

    class Meta:
        app_label = 'corpus'