from django.urls import path
# from . import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login_user, name='login'),

]