from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import serializerStudent,serializerGroup
from  .models import Group,Student
# Create your views here.
class ViewGroup(viewsets.ModelViewSet):
    serializer_class=serializerGroup
    queryset=Group.objects.all()

class ViewStudent(viewsets.ModelViewSet):
    serializer_class=serializerStudent
    queryset=Student.objects.all()