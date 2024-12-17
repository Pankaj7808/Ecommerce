from rest_framework import serializers
from .models import *
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class CategorySerializer(serializers.Serializer):
    model = Category
    fields = '__all__'