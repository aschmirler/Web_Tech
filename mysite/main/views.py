from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieList, Movie
# Create your views here.

def index(response, id):
	mv = MovieList.objects.get(id=id)

	return render(response,"main/mvlist.html",{"mv": mv})

def home(response):
	return render(response,"main/home.html",{})

def categories(response):
	cat = MovieList.objects.all()
	return render(response,"main/categories.html",{"cat":cat})

def Comedy(response):
	movies = Movie.objects.all()
	return render(response,"main/Comedy.html",{"movies":movies})
#
# def Horror(response):s
# 	return render(response,"main/Horror.html",{})
#
# def Romance(response):
# 	return render(response,"main/Romance.html",{})










