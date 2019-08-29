from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import State,City,Temperature
from .serializers import TemperatureSerializer
from rest_framework import status
import json


class WeatherPost(APIView):
    def post(self,request):
        file=request.data['json_file']
        # f = open(__file__, 'r')
        #
        # # read()
        # text = f.read(10)
        data = file.read().decode("utf-8")
        json_data = (json.loads(data))
        for data in json_data:
            json_data=data
            date = json_data['date']
            lat = json_data['location']['lat']
            lon = json_data['location']['lon']
            city = json_data['location']['city']
            state = json_data['location']['state']
            temperature = json_data['temperature']
            id = json_data['id']

            state, created = State.objects.get_or_create(state=state)
            location, created = City.objects.get_or_create(state=state, lat=lat, lng=lon, name=city)
            print(id, location, date, type(str(temperature)))
            Temperature.objects.create(id=id, city=location, date=date, temperature=str(temperature))
        return Response(
            {
                'message':'file red'
            }
        )

class WeatherDetail(APIView):
    def get(self,request,id):
        queryset=Temperature.objects.filter(id=id)
        print(queryset)
        serializer=TemperatureSerializer(queryset,many=True)
        return Response(
            {
                'data':serializer.data
            }
        )

class GetWeatherDetail(APIView):
    def get(self,request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        lat= request.GET.get('lat', None)
        lon= request.GET.get('lon', None)
        print(lat,lon)

        if start_date and end_date and lat and lon:
            queryset = Temperature.objects.filter(city__lat=lat, city__lng=lon, date__range=[start_date, end_date])

        elif start_date and end_date:
            queryset = Temperature.objects.filter(date__range=[start_date, end_date])

        elif lat and lon:
            queryset = Temperature.objects.filter(city__lat=lat, city__lng=lon)

        else:
            return Response(
                {
                    'Message': 'give lat,long or start_date,end_date or both in the get arguments'
                }
            )


        print(queryset)
        serializer=TemperatureSerializer(queryset,many=True)
        return Response(
            {
                'data':serializer.data
            }
        )


class DeleteWeather(APIView):
    def get(self,request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        lat= request.GET.get('lat', None)
        lon= request.GET.get('lon', None)
        print(lat,lon)

        if start_date and end_date and lat and lon:
            queryset = Temperature.objects.filter(city__lat=lat, city__lng=lon, date__range=[start_date, end_date])

        elif start_date and end_date:
            queryset = Temperature.objects.filter(date__range=[start_date, end_date])

        elif lat and lon:
            queryset = Temperature.objects.filter(city__lat=lat, city__lng=lon)

        else:
            return Response(
                {
                    'Message': 'give (lat,long) or (start_date,end_date) or both in the get arguments'
                }
            )
        queryset.delete()
        return Response(
            {
                'message':'weather object deleted '
            }
        )
