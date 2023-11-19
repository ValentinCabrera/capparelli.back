from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    USERNAME_FIELD = "id"

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

class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='groups')
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='users')