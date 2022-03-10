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

class Statistics(models.Model):
    Country = models.CharField(max_length=50)
    Code = models.CharField(max_length=5)
    NewConfirmed = models.IntegerField()
    TotalConfirmed = models.IntegerField()
    NewDeaths = models.IntegerField()
    TotalDeaths = models.IntegerField()
    NewRecovered = models.IntegerField()
    TotalRecovered = models.IntegerField()
    lastChange = models.DateTimeField(auto_now=True)
    lastUpdate = models.DateTimeField(auto_now_add=True)