from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Productserializer
from rest_framework.decorators import api_view
from .models import Product
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.

@api_view(['POST'])
def create_product(request):
    serializer = Productserializer(data = request.data)
    if serializer.is_valid():
        if request.data.get('quantity',0) > 0:
            serializer.validated_data['is_active'] = True
        else:
            serializer.validated_data['is_active'] = False
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def product_count(request):
    count = Product.objects.count()
    return Response({'product_count':count},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all(request):
    prod = Product.objects.all()
    serializer = Productserializer(prod, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

