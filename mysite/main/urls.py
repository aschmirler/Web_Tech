from django.urls import path
from . import views

urlpatterns = [
	path("<int:id>", views.index, name="index"),
	path("home",views.home,name="home"),
	path("categories/",views.categories,name="categories"),
	path("Comedy/",views.Comedy,name="comedy"),
	# path("Horror/",views.Horror,name="horror"),
	# path("Action/",views.Action,name="action"),
	# path("Romance/",views.Romance,name="romance"),
]
