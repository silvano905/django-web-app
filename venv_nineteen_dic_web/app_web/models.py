from django.db import models
from django.urls import reverse


class MakeWord(models.Model):
    english = models.CharField(max_length=20)
    spanish = models.CharField(max_length=20)
    sentence = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return self.english

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})