from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField(blank=False, null=False)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={'my_id': self.id})