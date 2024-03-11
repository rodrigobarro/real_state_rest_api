from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementSerializer


class AdvertisementList(APIView):

    def get(self, request, format=None):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvertisementDetail(APIView):

    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisement = self.get_object(pk)
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        advertisement_obj = self.get_object(pk)
        serializer = AdvertisementSerializer(advertisement_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        advertisement = self.get_object(pk)
        serializer = AdvertisementSerializer(advertisement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        advertisement = self.get_object(pk)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)