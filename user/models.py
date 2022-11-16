from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

# Create your models here.
from quiz.models import AbstractTimeStamp


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


phone_regex = RegexValidator(regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',message='Invalid phone number')


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    hint = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    verified_email = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, validators=[phone_regex], null=True, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-is_active']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'


class OTPModel(AbstractTimeStamp):
    """OTPModel to save otp value
    Args:
        contact_number: CharField
        otp_number: IntegerField
        expired_time: DateTimeField

    """
    contact_number = models.CharField(_('Contact Number'), max_length=20, null=False, blank=False)
    otp_number = models.IntegerField(_('OTP Number'), null=False, blank=False)
    verified_phone = models.BooleanField(default=False)
    expired_time = models.DateTimeField(_('Expired Time'), null=False, blank=False)

    def __str__(self):
        return self.contact_number

    class Meta:
        verbose_name = "OTPModel"
        verbose_name_plural = "OTPModels"
        db_table = 'otp_models'
