from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def endpoint(request):
    data = ['default', 'products', 'product/:detail', 'users', 'user/:detail']
    return Response(data)

@api_view(['GET', 'POST'])
def products(request):
    data = ['phone', 'cloth', 'etc']
    return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
def product(request, product_id):
    data = product_id
    return Response(data)

def users(request):
    data = ['ade', 'paul', 'gift']
    return Response(data)

def user_detail(request, user_id):
    data = user_id
    return Response(data)