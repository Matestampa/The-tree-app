from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status

from rest_framework import generics

from plantar.serializers import Trees_Serializer
from plantar.models import Plantados


@api_view(["GET"])
def all_trees(request):
	trees=Plantados.objects.filter(en_cuidado=True)
    
	serialized_trees=Trees_Serializer(trees,many=True)

	return Response(serialized_trees.data)