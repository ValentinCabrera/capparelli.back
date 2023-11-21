from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
import secrets
from back.utils.mail import send_email

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50, unique=True)

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

    def log_in(self, password):
        if self.check_password(password):
            token, created = Token.objects.get_or_create(user=self)

            return token

        return None

    def send_mail(self):
        if self.mail_check.count() > 0:
            self.mail_check.first().send_mail()

    def is_checked(self):
        return self.mail_check.count() == 0

class MailCheck(models.Model):
    token = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="mail_check")

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_hex(64)
        self.send_mail()
        super().save(*args, **kwargs)

    def check_token(self, token):
        if self.token == token:
            self.delete()
            return True

        return False

    def send_mail(self):
        subject = "Verificacion de mail."
        message = f"El token es el siguiente: {self.token}"
        recipient_list = [self.user.mail]
        send_email(subject, message, recipient_list)

class Client(User):
    phone_number = models.PositiveBigIntegerField()

class Admin(User):
    phone_number = models.PositiveBigIntegerField()
