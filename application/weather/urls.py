from django.urls import path, include
from .views import WeatherPost,WeatherDetail,GetWeatherDetail,DeleteWeather


urlpatterns = [
    path('file_read/', WeatherPost.as_view(), name='weather'),
    path('temp/<int:id>/', WeatherDetail.as_view(), name='weather_detail'),
    path('weather/', GetWeatherDetail.as_view(), name='weather_detail'),
    path('delete/', DeleteWeather.as_view(), name='weather_detail'),

    ]