from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile, Products
from .serializers import ProfileSerializer, ProductSerializer
from django.db.models import Q

# Create your views here.

@api_view(['GET'])
def endpoint(request):
    data = ['default', 'products', 'product/:id', 'users', 'user/:detail']
    return Response(data)

@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query is None:
            query =''
        productdata = Products.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        serializer = ProductSerializer(productdata, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        create_product = Products.objects.create(name=request.data['name'], category=request.data['category'], description=request.data['description'], price=request.data['price'])
        serializer = ProductSerializer(create_product, many=False)

@api_view(['GET', 'PUT', 'DELETE'])
def product(request, product_id):
    # data = username
    productdata = Products.objects.get(id=product_id)
    if request.method == 'GET':
        # productdata = productdata.objects.get(username=username)
        serializer = ProductSerializer(productdata)
        return Response(serializer.data)
    if request.method == 'PUT':
        productdata.name = request.data['name']
        productdata.category = request.data['category']
        productdata.description = request.data['description']
        productdata.price = request.data['price']
        productdata.save()
        serializer = ProductSerializer(productdata)
        return Response(serializer.data)

    if request.method == 'DELETE':
        productdata.delete()
        return Response("productdata deleted")


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query is None:
            query = ''

        usersprofile = Profile.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = ProfileSerializer(usersprofile, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        create_productdata = Profile.objects.create(username=request.data['username'], bio=request.data['bio'], residence=request.data['residence'], dob=request.data['dob'], user=request.data['user'])
        serializer =ProfileSerializer(create_productdata, many=False)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_detail(request, user_id):
    # data = username
    userdata = Products.objects.get(id=user_id)
    if request.method == 'GET':
        # productdata = productdata.objects.get(username=username)
        serializer = ProductSerializer(userdata)
        return Response(serializer.data)
    if request.method == 'PUT':
        userdata.name = request.data['name']
        userdata.category = request.data['category']
        userdata.description = request.data['description']
        userdata.price = request.data['price']
        userdata.save()
        serializer = ProductSerializer(userdata)
        return Response(serializer.data)

    if request.method == 'DELETE':
        userdata.delete()
        return Response("productdata deleted")