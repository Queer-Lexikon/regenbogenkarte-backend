from django.db import models

class Organisation(models.Model):
    country = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
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

    def __str__(self):
        return self.name

    def to_dict(self):
        opts = self._meta
        data = {}
        data['location'] = {}
        for f in opts.concrete_fields:
            if f.value_from_object(self):
                if f.name not in {'address', 'lat', 'lon', 'lat_lon_approx', 'id'}:
                    data[f.name] = f.value_from_object(self)
                elif f.name not in {'lat_lon_approx','id'}:
                    data['location'][f.name] = f.value_from_object(self)
                elif f.name != 'id':
                    data['location']['approx'] = f.value_from_object(self)
        return data

