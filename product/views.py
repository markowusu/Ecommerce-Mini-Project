# from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView    
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Product
from .serializers import ProductSerializer

class LatestProductList(APIView):

    def get(self,request, format=None):
        try:
            products = Product.objects.all()
        except self.Product.DoesNotExit:
            return Response(status = status.HTTP_404_NOT_FOUND )
        serializer = ProductSerializer(products, many= True)

        return Response(serializer.data)


class ProductDetails(APIView):
    def get_object(self, category_slug , product_slug):
        try:
            return Product.objects.filter(categories=category_slug).get(slug=product_slug)
        except self.Product.DoesNotExit:  
            raise Http404  

    def get(self,request, category_slug, product_slug, format=None):

        products = self.get_object(category_slug , product_slug )
        serializer = ProductSerializer(products)

        return Response(serializer.data)





