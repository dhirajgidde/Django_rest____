from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Tuterials
from .serializer import TuterialSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def tuterial_list(request):
    if request.method == 'GET':
        tutorials = Tuterials.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title_icontains=title)
        tuterials_serializer = TuterialSerializer(tutorials, many=True)
        return JsonResponse(tuterials_serializer.data, safe=False)
    elif request.method == 'POST':
        tuterial_data = JSONParser().parse(request)
        tuterial_serializer = TuterialSerializer(data=tuterial_data)
        if tuterial_serializer.is_valid():
            tuterial_serializer.save()
            return JsonResponse(tuterial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tuterial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tuterials.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tuterial_detail(request, pk):
    tutorial = Tuterials.objects.get(pk=pk)

    if request.method == 'GET':
        tutorial_serializer = TuterialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TuterialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    try:
        tutorial = Tuterials.objects.get(pk=pk)
    except Tuterials.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tuterial_list_published(request):
    tutorials = Tuterials.objects.filter(published=True)
    if request.method == 'GET':
        tutorials_serializer = TuterialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
