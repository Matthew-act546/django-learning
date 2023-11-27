from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(default="This is cool!")
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product:product", kwargs={'my_id': self.id})