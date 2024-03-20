from django.urls import path
from booking import views

urlpatterns = [
    path('bookings/', views.BookingList.as_view()),
    path('bookings/<uuid:pk>/', views.BookingDetails.as_view()),
    path('properties/', views.PropertyList.as_view()),
    path('properties/<uuid:pk>', views.PropertyDetail.as_view()),
    path('advertisements/', views.AdvertisementList.as_view()),
    path('advertisements/<uuid:pk>', views.AdvertisementDetail.as_view())
]