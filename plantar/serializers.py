from rest_framework import serializers
from .models import Plantados


class Trees_Serializer(serializers.ModelSerializer):
      class Meta:
            model=Plantados
            fields="__all__"
      

     

      

      