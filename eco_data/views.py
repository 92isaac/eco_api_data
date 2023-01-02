from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.db.models import Q

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
        create_developer = Profile.objects.create(username=request.data['username'], bio=request.data['bio'], residence=request.data['residence'], dob=request.data['dob'], user=request.data['user'])
        serializer =ProfileSerializer(create_developer, many=False)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def user_detail(request, user_id):
    data = user_id
    return Response(data)