from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.username', read_only=True)
    class Meta:
        model = models.Review
        fields = ['id', 'body', 'created', 'rating', 'reviewer','reviewer_name']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'