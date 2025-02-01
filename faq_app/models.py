from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
import asyncio

# Create your models here.
class FAQ(models.Model):
    question = models.TextField(verbose_name="Question")
    answer = RichTextField(verbose_name="Answer")
    question_hi = models.TextField(verbose_name="Question (Hindi)", blank=True)
    
    def __str__(self):
        return self.question
    
    async def translate_text_async(self, text, dest_lang):
        translator = Translator()
        try:
            translation = await translator.translate(text, dest=dest_lang)
            print(translation.text)
            return translation.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return text
    
    def translate_text(self, text, to_lang_code):
        return asyncio.run(self.translate_text_async(text, to_lang_code))
    
    def save(self, *args, **kwargs):
        if not self.question_hi:
            print("Saving in hindi")
            self.question_hi = self.translate_text(self.question, 'hi')
        super().save(*args, **kwargs)
        
    
    def get_translated_question(self, language_code):
        translation_field = f"question_{language_code}"
        return getattr(self, translation_field, self.question)
    
