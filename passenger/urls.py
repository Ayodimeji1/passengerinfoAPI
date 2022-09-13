from django.urls import path
from passenger import views

urlpatterns = [
    path('passengers/', views.passenger_list),
    path('passengers/<int:pk>/', views.passenger_detail)
]
