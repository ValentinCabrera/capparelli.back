from django.db import models
class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.surname