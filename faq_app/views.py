from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang_code'] = self.request.query_params.get('lang', 'en')
        return context

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang_code'] = self.request.query_params.get('lang', 'en')
        return context

