from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GroupSerializer, UseSerializer


# Create your views here.

# @api_view(["GET"])
# def home(request):

#     dicts = {
#         1: "WE are here",
#         2: "We are not here",
#         3: 12.5,
#         "Name": "Dhiraj Gidde",
#     }

#     content = dicts
#     return JsonResponse(content)

class UseViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UseSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
