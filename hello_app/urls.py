from django.urls import  include,  path
from . import views, customerformview
app_name='hello_app'
urlpatterns = [
    path('', views.index,name='index'),
    path('save_customer', views.save_customer,name='save_customer'),
    path('create_customer', customerformview.CustomerCreate, name='create_customer'),
]
