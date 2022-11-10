from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    phone = models.TextField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.name + " " + self.email