import re
from django.http import JsonResponse
from .models import PC
from .serializers import PCSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from try2 import serializers
@api_view(['GET','POST'])
def PC_list(request):
    #get all the pcs
    #serialize them
    #return json
    if(request.method == 'GET'):
        PCs = PC.objects.all()
        serializer = PCSerializer(PCs,many=True)
        return Response({"PCs" : serializer.data})
    if(request.method == 'POST'):
        serializer = PCSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response("Error",status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def PC_detail(request,id):
    try:
        pc = PC.objects.get(pk=id)
    except PC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PCSerializer(pc)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PCSerializer(pc,data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pc.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response("Method not existed!!!")
