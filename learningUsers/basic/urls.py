from django.urls import path,include
from basic import views

app_name='basic'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login',views.user_login,name='user_login')

]
