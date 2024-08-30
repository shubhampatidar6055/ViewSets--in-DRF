from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
# Create your views here.

#Viewsets

class StudentViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
    def update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data update sucessfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data updated partially"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        Stu = Student.objects.get(id=pk)
        Stu.delete()
        return Response({"msg":"Data deleted sucessfully"})



#ModelViewSet

# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class =StudentSerializer


#ReadOnlyModelViewSet

# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer