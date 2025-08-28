from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from .serializer import DutySerializer
from .models import Duty


# Create your views here.
def index(reguest):
    return HttpResponse('hello memei')

class DutyListCreate(APIView):
    def get(self,request):
        duties = Duty.objects.all()
        serializer = DutySerializer(duties, many=True)
        return Response(serializer.data)
    
    def Post(self, request):
        serializer = DutySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DutyDetail(APIView):
    def get(self, request, pk):
        duty = Duty.objects.get(pk=pk)
        serializer =DutySerializer(duty)
        return Response(serializer.data)

    def put(self, request, pk):
        duty = Duty.objects.get(pk=pk)
        serializer = DutySerializer(duty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        duty = Duty.object.get(pk=pk)
        duty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


