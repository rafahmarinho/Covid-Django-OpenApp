from rest_framework import serializers
from Statistics.models import Statistics

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Statistics 
        fields=('Country','Code','NewConfirmed','TotalConfirmed','NewDeaths','TotalDeaths','NewRecovered','TotalRecovered')