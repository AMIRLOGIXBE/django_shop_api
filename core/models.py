from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    message = models.TextField()