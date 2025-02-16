from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class ReviewViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication] 
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer