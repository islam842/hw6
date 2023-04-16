from django.urls import path
from phone_app.views import phone_all_view, phone_detail_view

urlpatterns = [
    path('phone_list/', phone_all_view, name='phone_list'),
    path('phone_list/<int:id>', phone_detail_view, name='phone_detail'),
]
