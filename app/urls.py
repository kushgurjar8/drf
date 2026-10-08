from django.urls import path
# from . import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',home, name='home'),
    path('get/',get_student, name='get'),
    path('create/',create_student, name='create'),
    path('create_json/',createstudentJSON, name='createjson'),
    path('create_ser/',CreateStudentSerializer, name='createserializer'),
    path('inbuilt_token/', obtain_auth_token, name='inbuilt_token'),
    path('dumy/', dumy, name='dumy'),
    path('update/<int:id>/',UpdateStudent, name='update'),
    path('patch/<int:id>/',PatchStudent, name='patch'),

]