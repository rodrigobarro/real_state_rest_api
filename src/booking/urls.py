from django.urls import path
from booking import views

urlpatterns = [
    path('', views.BookingList.as_view()),
    path('<uuid:pk>/', views.BookingDetails.as_view())
]