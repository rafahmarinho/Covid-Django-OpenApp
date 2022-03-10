from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json 
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Statistics.models import Statistics
from Statistics.serializers import StatisticsSerializer

import requests

# Create your views here.

@csrf_exempt
def home(request):

    return render(request, 'home.html')
    ################# ANOTHER API FOR TEST ##########################################
    # url = "https://covid-193.p.rapidapi.com/"
    # headers = {
    #     'x-rapidapi-host': "covid-193.p.rapidapi.com",
    #     'x-rapidapi-key': "3dfd196020msh33b576f1a39812bp17cf28jsnd8406c8b507e"
    # }
    #  querystring = {"search":"BRA"} // 'params=querystring' in line below
    # r = requests.request("GET", url + 'statistics/', headers=headers)
    # data = r.json()
    # namesCountriesFounded = data['response']
    # numbersCountriesFounded = data['results']
    # return render(request, 'home.html', {'namesCountriesFounded': namesCountriesFounded, 'numbersCountriesFounded': numbersCountriesFounded})

@csrf_exempt
def statistics(request):
    if request.method == 'GET':
        statistics = Statistics.objects.all()
        statistics_serializer = StatisticsSerializer(statistics, many=True)
        return JsonResponse(statistics_serializer.data,safe=False)
#       ===================TEST FRONT-END==========================
    # Uncomment the part below if you want to test the GET consumption of the API on the Front-end.
    #   ===========================================================
    #     libData = statistics_serializer.data[0]    
    #     libDataConvert = libData.values()
    #     libIndex = list(libDataConvert)

    #     context = {
    #     "libData": libData,
    #     "Country": libIndex,
    # }
        # return render(request, 'statistics.html', context)
# ===================================================
    elif request.method == 'POST':
        statistics_data = JSONParser().parse(request)
        statistics_serializer = StatisticsSerializer(data=statistics_data)
        if statistics_serializer.is_valid():
            statistics_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        ################ ANOTHER API FOR TEST ############################
        # url = "https://api.covid19api.com/countries"
        # payload = {}
        # headers = {}
        # r = requests.request("GET", url, headers=headers, data=payload)
        # data = r.json()

    elif request.method == 'PUT':
        statistics_data = JSONParser().parse(request)
        statistics = Statistics.objects.get(Country=statistics_data['Country'])
        statistics_serializer = StatisticsSerializer(
            statistics, data=statistics_data)
        if statistics_serializer.is_valid():
            statistics_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        department = statistics.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)