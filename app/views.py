from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializes import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .tokens import *

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




# # @api_view(['GET'])
# # @authentication_classes([TokenAuthentication])
# # @permission_classes([IsAuthenticated])
# # def dumy(request):
# #     return Response({'status': 200, 'message' : 'this is my dumy page',
# #                      "username" : request.user.username,
# #                      "email" : request.user.email,
# #                      "first_name" : request.user.first_name               
#     })


@api_view(['PUT'])
def UpdateStudent(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'status': 404, 'message': 'Student not found'})

    serialize = StudentSerializer(student, data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response({'status': 200, 'message': 'Student Updated', 'data': serialize.data})
    else:
        return Response({'status': 400, 'message': serialize.errors})


@api_view(['PATCH'])
def PatchStudent(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'status': 404, 'message': 'Student not found'})

    serialize = StudentSerializer(student, data=request.data, partial=True)
    if serialize.is_valid():
        serialize.save()
        return Response({'status': 200, 'message': 'Student PATCH Updated', 'data': serialize.data})
    else:
        return Response({'status': 400, 'message': serialize.errors})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def dumy(request):
    return Response({'status': 200, 'message' : 'this is my dumy page',
                     "username" : request.user.username,
                     "email" : request.user.email,
                     "first_name" : request.user.first_name          })




# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(username=username, password=password)

#     if user is not None:
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'message': 'Login successful',
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })

#     return Response({'message': 'Invalid username or password'})

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = MyToken.for_user(user)
        return Response({
            'message': 'Login successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    return Response({'message': 'Invalid username or password'})

