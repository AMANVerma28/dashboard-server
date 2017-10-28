from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
# Create your models here.

#Model class for analyticswell
class Well(models.Model):
    WID = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=30)
    location = models.PointField(default=Point(1,1),null=True)
    average_yield = models.DecimalField(max_digits=7,decimal_places=4)
    depth = models.FloatField(null = True,blank = False)
    def __str__(self):
        return "%s" %(self.WID)

#Model class for Yields
class Yield(models.Model):
    WID = models.ForeignKey(Well,to_field='WID',on_delete=models.CASCADE)
    Yield = models.FloatField(null = True, blank = True)
    Date = models.DateField(blank = False)
    def __str__(self):
        return "%s : %s" %(self.WID,self.Date)