from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price =  models.DecimalField(max_digits=8, decimal_places=2)
    seller_email = models.EmailField()
    posted_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
