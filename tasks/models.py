from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

class Task(models.Model):
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)