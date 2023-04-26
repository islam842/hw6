from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhoneListView.as_view(), name='phone_list'),
    path('phone_list/<int:id>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('add-phone_app/', views.CreatePhoneView.as_view(), name='create_phone'),
    path('phone_delete_list/', views.DeletePhoneListView.as_view()),
    path('phone_delete/<int:id>/delete/', views.DeletePhoneView.as_view(), name='delete_phone_view'),
    path('phone_update_list/', views.UpdatePhoneListView.as_view()),
    path('phone_update/<int:id>/update/', views.UpdatePhoneView.as_view(), name='update_phone_view'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('add-comment/', views.CreateCommentView.as_view(), name='comment'),
]