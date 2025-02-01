from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class FAQ(models.Model):
    question = models.TextField(verbose_name="Question")
    answer = RichTextField(verbose_name="Answer")
    question_hi = models.TextField(verbose_name="Question (Hindi)", blank=True)
    
    def __str__(self):
        return self.question
    
