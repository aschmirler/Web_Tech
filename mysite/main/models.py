from django.db import models

# Create your models here.
class MovieList(models.Model):
    name = models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movielist = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


