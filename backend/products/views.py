from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.

@api_view(['POST','PUT','PATCH','DELETE'])
def Products(request,pk = None):
    if request.method == 'POST':
        serializer = Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_active'] = request.data.get('quantity', 0) > 0
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if pk:
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = Productserializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method in ['PUT', 'PATCH']:
            partial = request.method == 'PATCH'
            serializer = Productserializer(product, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.validated_data['is_active'] = request.data.get('quantity', 0) > 0
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response({'message': 'Product deleted!'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'error': 'Invalid method or missing ID'}, status=status.HTTP_400_BAD_REQUEST)
 
    

@api_view(['GET'])
def product_count(request):
    count = Product.objects.count()
    return Response({'product_count':count},status=status.HTTP_200_OK)

@api_view(['GET'])
def all_products(request):
    prod = Product.objects.all()
    serializer = Productserializer(prod, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def all_active_product(request):
    prod = Category.objects.filter(is_active=True)
    serializer = CategorySerializer(prod,many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        categ = Category.objects.all()
        serializer = CategorySerializer(categ ,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET','PUT','DELETE'])
def categories(request,pk):
    if pk:
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'errors':'Category doesnt exists'},status=status.HTTP_404_NOT_FOUND)
    
        if request.method == 'GET':
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = CategorySerializer(category,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
        elif request.method == 'DELETE':
            category.delete()
            return Response({'message':'category deleted successfully'},status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid method or missing ID'}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET'])
def category_count(request):
    count = Category.objects.count()
    return Response({'Category count':count},status=status.HTTP_200_OK)
