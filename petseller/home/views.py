from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AnimalView(APIView):
    
    def get(self,request):
        return Response({
            'status':True,
            'message':'Fetching Data using GET'
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