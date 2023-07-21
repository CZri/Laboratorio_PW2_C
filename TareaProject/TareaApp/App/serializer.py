from rest_framework import  serializers
from .models    import  Group,Student
class  serializerGroup(serializers.ModelSerializer):
   class Meta:
      model=Group

      fields='__all__'

class serializerStudent(serializers.ModelSerializer):
  class Meta:
       model=Student
       fields='__all__'