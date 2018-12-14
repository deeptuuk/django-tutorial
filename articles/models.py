from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    archive = models.ForeignKey(Archive,on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})

class Archive(models.Model):
    name = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name
