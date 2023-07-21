from rest_framework import  serializers
from .models.Student import Student
from .models.Group import Group
class  serializerStudent(serializers.ModelSerializer):
   class Meta:
      model=Student
      #fields=('id','nombre','descripcion','precio','estado')
      fields='__all__'
class  serializerGroup(serializers.ModelSerializer):
   class Meta:
      model=Group
      #fields=('id','nombre','descripcion','precio','estado')
      fields='__all__'