from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import FAQ

class FAQAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq1 = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
        )
        self.faq2 = FAQ.objects.create(
            question="How does Django handle databases?",
            answer="Django uses ORM to interact with databases.",
        )

    def test_list_faqs(self):
        response = self.client.get("/api/faq/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_faq(self):
        response = self.client.get(f"/api/faq/{self.faq1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_translation_hindi(self):
        response = self.client.get(f"/api/faq/{self.faq1.id}/?lang=hi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("translated_question" in response.data)
