from django.urls import path
from property import views

urlpatterns = [
    path('', views.PropertyList.as_view()),
    path('<uuid:pk>/', views.PropertyDetail.as_view())
]