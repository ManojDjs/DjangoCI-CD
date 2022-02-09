from django.urls import path
from .views import User_detail,User_Edit
from django.conf.urls import include
urlpatterns = [

    path('User_Details/', User_detail.as_view(),name='User_Reg'),
    path('User_Edit/<int:pk>', User_Edit.as_view(),name='User_Edit')
]