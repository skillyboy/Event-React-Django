from rest_framework import serializers
from .models import *

from rest_framework import generics, filters
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Review, Rating, Product, Category



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LikedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedEvent
        fields = '__all__'
