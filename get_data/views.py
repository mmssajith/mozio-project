from django.contrib.gis.geos import Polygon, Point
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Providers, Polygons
from .serializers import ProviderSerializer, PolygonSerializer


# Endpoints for PROVIDERS
@api_view(['GET'])
def get_all_provider(request):
    snippets = Providers.objects.all()
    serializer = ProviderSerializer(snippets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_provider(request, name):
    snippets = Providers.objects.get(name=name)
    serializer = ProviderSerializer(snippets, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_single_provider(request, name):
    snippets = Providers.objects.get(name=name)
    serializer = ProviderSerializer(snippets, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_single_provider(request, name):
    snippets = Providers.objects.get(name=name)
    snippets.delete()
    return Response("Delete Successful")

@api_view(['POST'])
def new_provider(request):
    serializer = ProviderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # save to db
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoints for POLYGONS
@api_view(['GET'])
def get_single_area(request, id, name):
    provider = Providers.objects.get(name=name)
    polygons = Polygons.objects.filter(Providers=provider).get(pk=id)
    serializer = PolygonSerializer(polygons, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_area_by_provider(request, name):
    provider = Providers.objects.get(name=name)
    polygons = Polygons.objects.filer(Providers=provider)
    serializer = PolygonSerializer(polygons, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_area(request, name, pk):
    provider = Providers.objects.get(name=name)
    if len(request.data['area']['coordinates']) == 1:
        polygon_data = Polygon(
            request.data['area']['coordinates'][0], [])
    elif len(request.data['area']['coordinates']) == 2:
        polygon_data = Polygon(
            request.data['area']['coordinates'][0],
            request.data['area']['coordinates'][1])
    else:
        return Response("Bad geojson data")
    polygons = Polygons.objects.create(
        name=request.data['name'],
        price=request.data['price'],
        provider=provider,
        service_area=polygon_data
    )
    serializer = PolygonSerializer(polygons, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_area(request, id, name):
    provider = Providers.objects.get(name=name)
    polygons = Polygons.objects.filter(Providers=provider).get(pk=id)
    serializer = PolygonSerializer(polygons, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_single_area(request, id, name):
    provider = Providers.objects.get(name=name)
    polygons = Polygons.objects.filter(Providers=provider).get(pk=id)
    polygons.delete()
    return Response("Polygon Deleted Successfully")

# Polygon Querying
@api_view(['GET'])
def query_data(request):
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    if lat == None or lng == None:
        return Response("Bad Query")
    point = Point(lat, lng)
    query_set = Polygons.objects.filter(service_area__contains=point)
    serializer = PolygonSerializer(query_set, many=True)
    return Response(serializer.data)