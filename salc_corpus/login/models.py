from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'login'
        ordering = ["-c_time"]
        verbose_name = "user"
        verbose_name_plural = "users"