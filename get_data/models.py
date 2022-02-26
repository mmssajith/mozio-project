from django.contrib.gis.db import models

# Create your models here.
class Providers(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Polygons(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE)

    service_area = models.PolygonField()

    def __str__(self):
        return self.name
