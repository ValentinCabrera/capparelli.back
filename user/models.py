from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
import secrets
from back.utils.mail import async_email
from django.utils import timezone
class UserManager(BaseUserManager):
    def create_user(self, mail, name, surname, password=None, **extra_fields):
        mail = self.normalize_email(mail)
        user = self.model(mail=mail, name=name, surname=surname, **extra_fields)
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, name, surname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(mail, name, surname, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50, unique=True)
    state = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "mail"
    REQUIRED_FIELDS = ["name", "surname"]

    objects = UserManager()

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mail_check")

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
        context = {"token": self.token, "url":"https://www.youtube.com", "name":self.user.name}
        recipient_list = [self.user.mail]
        async_email(subject=subject, recipient_list=recipient_list, context=context)