from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        
        lang_code = self.request.query_params.get('lang', 'en')
        queryset = FAQ.objects.all()

