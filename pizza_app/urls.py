from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/pizza_list/', views.pizza_List),
    path('api/v1/pizza_list/<int:pk>/', views.pizza_Detail),
    path('api/v1/pizza_list/<slug:ty>/<slug:si>/', views.pizza_size_and_type),
]