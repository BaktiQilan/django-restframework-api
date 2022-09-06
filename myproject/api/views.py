import imp
from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items =  Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def oneData(request, pk):
    try:
        items = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(items)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(instance=items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

