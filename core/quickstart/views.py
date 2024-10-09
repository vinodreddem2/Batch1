# from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def index(request):
    courses={
        "id":1,
        "course_name":"Django_Rest_FrameWork"
    }
    return Response(courses)

@api_view(["GET",'POST','PUT','PATCH','DELETE'])
def person(request):
    # if we want to get the data 
    if request.method=="GET":
        # Query the data from the database ---> Return QuerySet 
        data = Person.objects.all() 
        # Serialize the queryset into json format
        serializer = PersonSerializer(data,many=True)
       
        return Response(serializer.data) 
    
    # if we want to post the data
    elif request.method=="POST":
        
        data = request.data
        
        serializer = PersonSerializer(data = data)
        
        # Validate the data that needs to be stored in the DB , is it in the required format ?
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors) 
    # Full Update
    elif request.method=="PUT":
        
        data = request.data
        
        serializer = PersonSerializer(data = data)
        
        # Validate the data that needs to be stored in the DB , is it in the required format ?
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)     
    # Partial Update
    elif request.method == "PATCH":
        
        data = request.data
        
        # Getting the data from data base using the id
        obj = Person.objects.get(id=data['id'])
        
        serializer = PersonSerializer(obj,data = data,partial=True)
        
        # Validate the data that needs to be stored in the DB , is it in the required format ?
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    else:
        data = request.data
        
        obj = Person.objects.get(id=data['id'])
        
        obj.delete()
        
        return Response(f' The requested object is deleted')