from django.db import models
from django.urls import reverse

class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.pk])

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('pk',)
        unique_together = ('list', 'text')
    def __str__(self):
        return f'{self.text}'