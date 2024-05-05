from django.db import models

# Create your models here.

class empresa(models.Model):
    name = models.CharField(max_length=100)
    usernameComputrabajo = models.CharField(max_length=100, blank=True, null=True)
    usernameInstagram = models.CharField(max_length=100, blank=True, null=True)
    usernameFacebook = models.CharField(max_length=100, blank=True, null=True)