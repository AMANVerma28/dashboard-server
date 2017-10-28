from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import detail_route
from rest_framework import renderers
from .models import *
from .serializers import *

# Create your views here.

#View method for model Well
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def welldetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Well.objects.all()   
        serializer = WellSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Yield
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def yielddetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Yield.objects.all()   
        serializer = YieldSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)