from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def endpoint(request):
    data = ['default', 'products', 'product/:detail', 'user']
    return Response(data)

@api_view(['GET', 'POST'])
def products(request):
    data = ['phone', 'cloth', 'etc']
    return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
def product(request, product_id):
    data = product_id
    return Response(data)