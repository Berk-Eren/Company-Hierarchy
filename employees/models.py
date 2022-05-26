from django.db import models
from django.contrib.auth.models import AbstractUser

from companies.models import Company
from positions.models import Position


class Employee(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        pre_text = "{}".format(self.username)

        if self.position:
            pre_text += " : {}".format(self.position.department.title)
        if self.company:
            pre_text += " : {}".format(self.company.title)
        
        return pre_text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)