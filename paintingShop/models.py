from django.db import models

# Create your models here.

class Painting(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200, default="Jaka cena??")
    size = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title