from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

class Client(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    USERNAME_FIELD = "id"

    def __str__(self):
        return self.name + ' ' + self.surname

    def save(self, *args, **kwargs):
        try:
            old_password = Client.objects.get(pk=self.pk).password

            if old_password != self.password:
                self.password = make_password(self.password)

        except:
            self.password = make_password(self.password)

        super(Client, self).save(*args, **kwargs)

class Admin(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    USERNAME_FIELD = "id"

    def __str__(self):
        return self.name + ' ' + self.surname

    def save(self, *args, **kwargs):
        try:
            old_password = Admin.objects.get(pk=self.pk).password

            if old_password != self.password:
                self.password = make_password(self.password)

        except:
            self.password = make_password(self.password)

        super(Admin, self).save(*args, **kwargs)