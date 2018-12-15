from django.db import models
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    archive = models.ForeignKey('Archive',on_delete=models.PROTECT,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def snippet(self):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        tmp = strip_tags(md.convert(self.body))[:100]
        return tmp

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})

class Archive(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:archive-detail', kwargs={'pk': self.pk})
