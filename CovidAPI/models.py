from django.db import models

# Create your models here.

# Sample of the data returned:

# {
# "country": "Ireland",
# "code": "IE",
# "confirmed": 480846,
# "recovered": 401907,
# "critical": 89,
# "deaths": 5566,
# "latitude": 53.41291,
# "longitude": -8.24389,
# "lastChange": "2021-11-11T15:49:04+01:00",
# "lastUpdate": "2021-11-11T17:15:03+01:00"
# }

class Location(models.Model):
    Country = models.CharField(max_length=50)
    Code = models.CharField(max_length=5)
    
class StatisticsCVD(models.Model):
    Confirmed = models.IntegerField()
    Recovered = models.IntegerField()
    Critical = models.IntegerField()
    Deaths = models.IntegerField()

class Logs(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    lastChange = models.DateTimeField(auto_now=True)
    lastUpdate = models.DateTimeField(auto_now_add=True)