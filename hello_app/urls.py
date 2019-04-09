from django.urls import  include,  path
from . import views
app_name='hello_app'
urlpatterns = [
    path('', views.index,name='index'),
]
