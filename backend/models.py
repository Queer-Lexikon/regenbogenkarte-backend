from django.db import models

class Organisation(models.Model):
    state = models.ForeignKey("State", on_delete=models.RESTRICT)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 256, blank = True)
    website = models.CharField(max_length = 200, blank = True)
    phone = models.CharField(max_length = 100, blank = True)
    address = models.CharField(max_length = 100, blank = True)
    lon = models.FloatField()
    lat = models.FloatField()
    lat_lon_approx = models.BooleanField(null = True)
    activities = models.TextField(blank = True)
    identities = models.CharField(max_length = 500, blank = True)
    age_restriction = models.CharField(max_length = 100, blank = True)

    @property
    def country(self):
        return self.state.country

    def __str__(self):
        return self.name

    def to_dict(self):
        data = {
            "country": self.country.name,
            "state": self.state.name,
            "name": self.name,
            "email": self.email,
            "website": self.website,
            "phone": self.phone,
            "location": {
                "address": self.address,
                "lon": self.lon,
                "lat": self.lat,
                "approx": self.lat_lon_approx,
            },
            "activities": self.activities,
            "identities": self.identities,
            "age_restriction": self.age_restriction,
        }
        return data

class Country(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length = 50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["country", "name"]

