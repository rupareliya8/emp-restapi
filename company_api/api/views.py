from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import CompanySerializer,EmployeeSerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer