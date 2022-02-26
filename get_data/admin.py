from django.contrib import admin
from .models import Providers, Polygons

# Adding the Providers model to the admin site.
admin.site.register(Providers)
admin.site.register(Polygons)