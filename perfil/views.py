from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#----------serializers-----------------
from .serializers import Profile_serializer

#----------models---------------------
from acceso.models import Profile



@api_view(["GET"])
def particular_profile(request,id):
    
    profile=Profile.objects.get(id=id)

    serialized_prof=Profile_serializer(profile)

    return Response(serialized_prof.data,status=status.HTTP_200_OK)

