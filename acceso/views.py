from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User_data, User_access,Profile


@api_view(["GET"])

def login(request):
    pass


def signup(request):
    pass