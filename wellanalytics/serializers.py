from rest_framework import serializers
from wellanalytics.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

#Serializer Class for model Well
class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

#Serializer Class for model Yield
class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = '__all__'