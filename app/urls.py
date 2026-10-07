from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('get/',get_student, name='get'),
    path('create/',create_student, name='create'),
    path('create_json/',createstudentJSON, name='createjson'),
    path('create_ser/',CreateStudentSerializer, name='createserializer'),

]