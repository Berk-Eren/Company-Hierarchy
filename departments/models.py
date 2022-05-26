from django.db import models
from companies.models import Company


class Department(models.Model):
    title = models.CharField(max_length=150, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('title', 'company'), )

    def __str__(self):
        return "{} : {}".format(self.company.title, self.title)