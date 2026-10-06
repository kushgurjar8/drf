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

