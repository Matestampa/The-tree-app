from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status

from .models import Plantados

@api_view(["GET"])
def all_trees(request):
	tress=Plantados.objects.all()

	serialized_trees=Trees_Serializer(trees,many=True)

	return Response(serialized_trees.data,status=status.HTTP_200_OK)


