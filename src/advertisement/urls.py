from django.urls import path
from advertisement import views

urlpatterns = [
    path('', views.AdvertisementList.as_view()),
    path('<uuid:pk>/', views.AdvertisementDetail.as_view())
]