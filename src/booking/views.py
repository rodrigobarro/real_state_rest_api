from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Booking, Advertisement, Property
from booking.serializers import BookingSerializer, PropertySerializer, AdvertisementSerializer


class BookingList(APIView):

    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        check_in_date = request.data['check_in_date']
        check_out_date = request.data['check_out_date']

        if check_out_date < check_in_date:
            return Response('Check-out date cannot be before check-in date', 
                            status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetails(APIView):

    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        advertisement = self.get_object(pk)
        serializer = BookingSerializer(advertisement)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        advertisement = self.get_object(pk)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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