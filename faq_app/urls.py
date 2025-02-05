from django.urls import path
from .views import FAQList, FAQDetail

urlpatterns = [
    path("", FAQList.as_view(), name="faq-list"),
    path("<int:pk>/", FAQDetail.as_view(), name="faq-detail"),
]
