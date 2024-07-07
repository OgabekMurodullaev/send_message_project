from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    sender = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.sender

    def get_absolute_url(self):
        return reverse(viewname='xabarlar')
