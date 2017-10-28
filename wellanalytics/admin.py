from django.contrib.gis import admin
from .models import *

# Register your models here.

#Open Street Maps Geo Admin is used.
admin.site.register(Well,admin.OSMGeoAdmin)
admin.site.register(Yield,admin.OSMGeoAdmin)