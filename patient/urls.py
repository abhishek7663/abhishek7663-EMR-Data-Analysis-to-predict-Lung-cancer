from django.urls import path
from .import views

urlpatterns=[
    path('',views.index, name='index'),
    path('index.html',views.index,name='index'),
    path('register.html',views.register,name='register'),
    path('login.html',views.login,name='login'),
    path('contact.html',views.contact,name='contact'),
    path('logout.html',views.logout,name='logout'),
    path('home.html',views.home,name='home'),
    path('cancer.html', views.cancer,name='cancer'),
    path('predict.html', views.predict,name='predict'),

]