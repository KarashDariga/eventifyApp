from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    info = models.TextField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


