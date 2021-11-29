from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status

from rest_framework import generics

from .serializers import Trees_Serializer
from .models import Plantados


@api_view(["POST"])
def new_tree(request):
	
	new_tree=Trees_Serializer(data=request.data)

	if new_tree.is_valid():
	   new_tree.save()
	   return Response("Arbol añadido con exito",status=status.HTTP_201_CREATED)
	
	else:
	   return Response(new_tree.errors)


