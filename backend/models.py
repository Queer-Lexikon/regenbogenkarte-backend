from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Organisation(models.Model):
    state = models.ForeignKey("State", on_delete=models.RESTRICT)
    name = models.CharField(max_length = 100)
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

    @property
    def emails(self):
        return self.orgemail_set.as_list() 

    @property
    def phones(self):
        return self.orgphone_set.as_list() 

    @property
    def websites(self):
        return self.orgwebsite_set.as_list() 

    def __str__(self):
        return self.name

    def to_dict(self):
        data = {
            "country": self.country.name,
            "state": self.state.name,
            "name": self.name,
            "email": self.emails[0]["email"] if self.emails else None,
            "emails": self.emails,
            "website": self.websites[0]["url"] if self.websites else None,
            "websites": self.websites,
            "phone": self.phones[0]["phone"] if self.phones else None,
            "phones": self.phones,
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

class OrgContactManager(models.Manager):
    def as_list(self):
        return [obj.as_dict() for obj in self.all()]

class OrgContact(models.Model):
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)
    label = models.CharField(max_length = 30)

    objects = OrgContactManager()
    def as_dict(self):
        pass

    class Meta:
        abstract = True


class OrgEmail(OrgContact):
    label = models.CharField(max_length = 30, default="E-Mail")
    email = models.EmailField()

    def as_dict(self):
        return {"label": self.label, "email": self.email}

    class Meta:
        verbose_name = "e-mail"

class OrgPhone(OrgContact):
    label = models.CharField(max_length = 30, default="Telefon")
    phone = PhoneNumberField()

    def as_dict(self):
        return {"label": self.label, "phone": self.phone.as_international}

    class Meta:
        verbose_name = "phone"

class OrgWebsite(OrgContact):
    label = models.CharField(max_length = 30, default="Website")
    url = models.URLField()

    def as_dict(self):
        return {"label": self.label, "url": self.url}

    class Meta:
        verbose_name = "website"



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

