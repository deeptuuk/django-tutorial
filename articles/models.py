from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    thumb = mdoels.ImageField(default='default.png', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
