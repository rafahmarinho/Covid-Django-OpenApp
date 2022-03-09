from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CovidAPI.models import Location, StatisticsCVD, Logs
from CovidAPI.serializers import LocationSerializer, StatisticsCVDSerializer, LogsSerializer

import requests

# Create your views here.


def home(request):
    url = "https://covid-193.p.rapidapi.com/"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "3dfd196020msh33b576f1a39812bp17cf28jsnd8406c8b507e"
    }

    # querystring = {"search":"BRA"} // 'params=querystring' in line below
    r = requests.request("GET", url + 'countries/', headers=headers)
    data = r.json()
    namesCountriesFounded = data['response']
    numbersCountriesFounded = data['results']
    return render(request, 'home.html', {'namesCountriesFounded': namesCountriesFounded, 'numbersCountriesFounded': numbersCountriesFounded})


def countries(request):
    url = "https://covid-193.p.rapidapi.com/"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "3dfd196020msh33b576f1a39812bp17cf28jsnd8406c8b507e"
    }

    # querystring = {"search":"BRA"} // 'params=querystring' in line below
    r = requests.request("GET", url + 'countries/', headers=headers)
    data = r.json()
    namesCountriesFounded = data['response']
    numbersCountriesFounded = data['results']
    return render(request, 'countries.html', {'namesCountriesFounded': namesCountriesFounded, 'numbersCountriesFounded': numbersCountriesFounded})


def statistics(request):
    url = "https://covid-193.p.rapidapi.com/"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "3dfd196020msh33b576f1a39812bp17cf28jsnd8406c8b507e"
    }

    # querystring = {"search":"BRA"} // 'params=querystring' in line below
    r = requests.request("GET", url + 'statistics/', headers=headers)
    data = r.json()
    TotalCountries = data['results']
    Continent = data['response'][0]['country']
    return render(request, 'statistics.html', {'TotalCountries': TotalCountries, 'Continent': Continent})


# def home(request):
#     URL = "http://maps.googleapis.com/maps/api/geocode/json"

#     # location given here
#     location = "delhi technological university"

#     # defining a params dict for the parameters to be sent to the API
#     PARAMS = {'address':location}

#     # sending get request and saving the response as response object
#     r = requests.get(url = URL, params = PARAMS)

#     # extracting data in json format
#     data = r.json()


#     # extracting latitude, longitude and formatted address
#     # of the first matching location
#     latitude = data['results'][0]['geometry']['location']['lat']
#     longitude = data['results'][0]['geometry']['location']['lng']
#     formatted_address = data['results'][0]['formatted_address']

#     # printing the output
#     print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#         %(latitude, longitude,formatted_address))


# Location

# print(response.text)
# response=requests.get('https://covid-193.p.rapidapi.com/countries').json()

# def LocationAPI(request,id=0):
#     if request.method=='GET':
#         Location = Location.objects.all()
#         Location_serializer=LocationSerializer(Locations,many=True)
#         return JsonResponse(Locations_serializer.data,safe=False)
#     elif request.method=='POST':
#         Location_data=JSONParser().parse(request)
#         Locations_serializer=LocationSerializer(data=Location_data)
#         if Locations_serializer.is_valid():
#             Locations_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         Location_data=JSONParser().parse(request)
#         Location=Locations.objects.get(LocationId=Location_data['LocationId'])
#         Locations_serializer=LocationSerializer(Location,data=Location_data)
#         if Locations_serializer.is_valid():
#             Locations_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         Location=Locations.objects.get(LocationId=id)
#         Location.delete()
#         return JsonResponse("Deleted Successfully",safe=False)
