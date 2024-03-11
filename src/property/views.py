from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from property.models import Property
from property.serializers import PropertySerializer


class PropertyList(APIView):

    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyDetail(APIView):

    def get_object(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        property_obj = self.get_object(pk)
        serializer = PropertySerializer(property_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        property = self.get_object(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)