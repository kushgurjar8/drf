from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializes import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({'status': 200, 'message': 'This is Home page'})

@api_view(['GET'])
def get_student(request):
    student = Student.objects.all()
    serialize = StudentSerializer(student, many=True)
    return Response({'status': 200, 'data': serialize.data})


@api_view(['POST'])
def create_student(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    number = request.POST.get('number')

    if request.method == 'POST':
        Student.objects.create(name=name, age=age, email=email, number=number)
        return Response({'status': 200, 'message': 'Student Created'})


@api_view(['POST'])
def createstudentJSON(request):
    name = request.data.get('name')
    age = request.data.get('age')
    email = request.data.get('email')
    number = request.data.get('number')

    if request.method == 'POST':
        Student.objects.create(name=name, age=age, email=email, number=number)
        return Response({'status': 200, 'message': 'Student Created'})

@api_view(['POST'])
def CreateStudentSerializer(request):
    data = request.data
    serialize = StudentSerializer(data=data)
    if serialize.is_valid():
        serialize.save()
        return Response({'message': 'succesfull'})
    else:
        return Response({'message': serialize.errors})    
