from django.db import models

# Create your models here.
class Travel(models.Model):
    attraction = models.CharField(max_length=200)
    slug = models.SlugField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    timing = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.attraction