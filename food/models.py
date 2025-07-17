from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
