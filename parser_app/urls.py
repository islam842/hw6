from django.urls import path
from . import views

urlpatterns = [
    path('start_parsing/', views.ParseFormFilmView.as_view(), name='parser'),
    path('film_parse_list/', views.ParseFilmListView.as_view(), name='film_list'),
]