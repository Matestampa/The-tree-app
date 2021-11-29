from rest_framework import serializers

from plantar.serializers import Trees_Serializer

from acceso.models import Profile



class Profile_serializer(serializers.ModelSerializer):
      class Meta:
            model=Profile
            fields="__all__"
      

      def to_representation(self, instance):
          data=super().to_representation(instance)
          data["username"]=instance.get_username()

          arboles=Trees_Serializer(instance.plantados_set.all(),many=True)

          data["arboles_propios"]=arboles.data

          return data
            