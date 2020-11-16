from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classess = (IsAuthenticated)

    def get(self, request):
        content = {'Message': 'Hello,GeeksforGeeks'}
        return Response(content)
