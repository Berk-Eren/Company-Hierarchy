from django.db import models

import employees.models
from departments.models import Department


class Position(models.Model):
    title = models.CharField(max_length=150, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('title', 'department'), )

    def __str__(self):
        return "{} : {} : {}".format(self.department.company.title, 
                                        self.department.title,
                                            self.title)

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        
        return super().save(*args, **kwargs)

    def is_filled(self):
        return employees.models.Employee.objects.filter(position=self)\
                                                .exists()
