from django.db import models
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Tag)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
