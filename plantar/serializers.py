from rest_framework import serializers
from .models import Plantados

from random import randint

def text_to_coords(text):#como no tenemosla api lo simulamos de forma random
    coord=""
    for i in range(20):
        if i==10:
           coord+=";"
        else:
           coord+=str(randint(1,10))
    
    return coord

    



class Trees_Serializer(serializers.ModelSerializer):
      class Meta:
            model=Plantados
            fields="__all__"
      
      
      #---------------representacion de la info al momento de devolverla------------------
      
      def to_representation(self, instance):
          response=super().to_representation(instance)
          response["ult_regado"]=instance.get_ult_regado()
          response["arbol_gen"]=str(instance.arbol_gen)
          response["dueño_username"]=str(instance.dueño.get_username())

          return response
      

      #---------------validaciones al subir------------------------------------------------
     
      def create(self,validated_data):
          validated_data["ubi_coord"]=text_to_coords(validated_data["ubi_text"])#aca llamariamos a la api de google maps

          return Plantados.objects.create(**validated_data)

     

      

      