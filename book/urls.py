from django.urls import path
from book.views import bookview

urlpatterns = [
    path('book/', bookview, name='book'),
]