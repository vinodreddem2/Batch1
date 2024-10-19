from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer
# Create your views here.

class AnimalView(APIView):
    
    def get(self,request):
        
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset,many=True)
        
        return Response({
            'status':True,
            'message':'Fetching Data using GET',
            'data':serializer.data
        })
    
    def post(self,request):
        return Response({
            'status':True,
            'message':'Fetching Data using POST'
        }) 
    
    def put(self,request):
        return Response({
            'status':True,
            'message':'Fetching Data using PUT'
        })
    
    def patch(self,request):
        return Response({
            'status':True,
            'message':'Fetching Data using PATCH'
        })