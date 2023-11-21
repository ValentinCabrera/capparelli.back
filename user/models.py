from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = "mail"

    def __str__(self):
        return self.name + ' ' + self.surname

    def save(self, *args, **kwargs):
        try:
            old_password = User.objects.get(pk=self.pk).password

            if old_password != self.password:
                self.password = make_password(self.password)

        except:
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)

    def is_from_group(self, Model, pk):
        try:
            return Model.objects.get(pk=pk)

        except:
            return None

    def get_user_group(self):
        if self.is_from_group(Client, self.pk):
            return "Client"

        elif self.is_from_group(Admin, self.pk):
            return "Admin"

        else:
            return "None"

    def is_admin_group(self):
        return self.get_user_group() == "Admin"


class Client(User):
    phone_number = models.PositiveBigIntegerField()

class Admin(User):
    phone_number = models.PositiveBigIntegerField()
