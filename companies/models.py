from django.db import models
from django.core.exceptions import ValidationError


class Company(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title