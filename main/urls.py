from django.urls import path
from .views import CountryAPIView


urlpatterns = [
    path('countries/', CountryAPIView.as_view()),
    path('countries/<int:pk>/', CountryAPIView.as_view()),

]