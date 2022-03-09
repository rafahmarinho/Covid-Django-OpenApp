from rest_framework import serializers
from CovidAPI.models import Location,StatisticsCVD,Logs

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location 
        fields=('Country','Code')

class StatisticsCVDSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatisticsCVD 
        fields=('Confirmed','Recovered','Department','Critical','Deaths')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logs 
        fields=('latitude','longitude','lastChange','lastUpdate')