from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Tag)
    text = models.TextField()

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
