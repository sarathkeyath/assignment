from django.shortcuts import render

from rest_framework import serializers,viewsets
from rest_framework.decorators import  action
from rest_framework.response import Response

from .models import *

import csv 

from django.core.files.base import ContentFile
from django.core.files.storage  import FileSystemStorage

fs = FileSystemStorage(location= 'tmp/')

# Create your views here.

#serializer
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self,request):  
        file = request.FILES['file']
        content = file.read()

        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv",file_content
        )

        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file,errors= "ignored")
        reader = csv.reader(csv_file)
        next(reader)

        company_list = []
        for id_, row in enumerate(reader):
            (
                company_name,
                
            ) = row

            company_list.append(
                Company(
                    company_name = company_name,
                )
            )
        Company.objects.bulk_create(company_list)
        return Response("Successfully uploaded the data")
 


class EmployeeViewSet(viewsets.ModelViewSet):
    querysett = Company.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self,request):  
        file = request.FILES['file']
        content = file.read()

        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv",file_content
        )

        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file,errors= "ignored")
        reader = csv.reader(csv_file)
        next(reader)

        employee_list = []
        for id_, row in enumerate(reader):
            (
                employee_id ,
                first_name ,
                last_name ,
                phone_number ,
                Company_namee ,
                salary ,
                manager_id ,
                department_id ,
                fkey
                
            ) = row

            employee_list.append(
                Employee(
                    employee_id =  employee_id ,
                    first_name = first_name ,
                    last_name = last_name,
                    phone_number = phone_number,
                    Company_namee  =  Company_namee,
                    salary  = salary,
                    manager_id  = manager_id ,
                    department_id  = department_id,
                    fkey_id = fkey,
                )
            )
        Employee.objects.bulk_create(employee_list)
        return Response("Successfully uploaded the data")
 
