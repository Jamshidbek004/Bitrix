from django.urls import path
from . import views

urlpatterns = [
    path('', views.royxat_list, name='royxat_list'),
    path('create/', views.create_royxat, name='create_royxat'),
    path('update/<int:pk>/', views.update_royxat, name='update_royxat'),
    path('filter/<str:status>/', views.filter_royxat_by_status, name='royxat_detail'),  # Parameterized URL
]
