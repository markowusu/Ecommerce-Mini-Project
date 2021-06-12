from rest_framework import serializers
from .models import Category , Product

class ProductSerializer(serializers.ModelSerializer ):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    image =  serializers.CharField(source='get_image', read_only=True)
    thumbnail_image =  serializers.CharField(source='get_thumbnail_image', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'brand',
            'description',
            'price',
            'url',
            'old_price',
            'quantity',
            'image',
            'thumbnail_image',      
        )