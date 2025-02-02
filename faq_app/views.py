from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from rest_framework.response import Response


# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["lang_code"] = self.request.query_params.get("lang", "en")
        return context


class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["lang_code"] = self.request.query_params.get("lang", "en")
        return context

    def retrieve(self, request, *args, **kwargs):
        faq_id = self.kwargs.get("pk")
        lang_code = self.request.query_params.get("lang", "en")

        cache_key = f"faq_{faq_id}_{lang_code}"
        cached_faq = cache.get(cache_key)
        print(cached_faq)
        if cached_faq is not None:
            return Response(cached_faq)

        faq = FAQ.objects.get(id=faq_id)
        serialized_faq = FAQSerializer(faq, context={"lang_code": lang_code})
        cache.set(cache_key, serialized_faq.data, timeout=60 * 60)
        return Response(serialized_faq.data)
