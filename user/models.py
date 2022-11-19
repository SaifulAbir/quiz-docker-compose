from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

# Create your models here.
from quiz.models import AbstractTimeStamp


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        username = self.model.normalize_username(username)
        user = self.model(
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

phone_regex = RegexValidator(regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',message='Invalid phone number')


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    GENDER_TYPES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    full_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    gender=models.CharField(max_length=20, blank=True, null=True,
                                     choices=GENDER_TYPES)
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
    phone = models.CharField(max_length=255, validators=[phone_regex])
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        if self.phone:
            return self.phone
        if self.email:
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
    contact_number = models.CharField(_('Contact Number'), max_length=255, validators=[phone_regex], null=False, blank=False)
    otp_number = models.IntegerField(_('OTP Number'), null=False, blank=False)
    verified_phone = models.BooleanField(default=False)
    expired_time = models.DateTimeField(_('Expired Time'), null=False, blank=False)

    def __str__(self):
        return self.contact_number

    class Meta:
        verbose_name = "OTPModel"
        verbose_name_plural = "OTPModels"
        db_table = 'otp_models'
