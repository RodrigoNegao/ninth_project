from __future__ import unicode_literals
import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.urls import reverse
# Install Pillow and django-imagekit
from PIL import Image
# Signals
from django.db.models import signals
from django.dispatch import receiver
# from django.db.models.signals import post_save

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password,is_staff, is_superuser, **extra_fields):
        #Creates and saves a User with the given email and password.
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
        is_staff=is_staff, is_active=True,
        is_superuser=is_superuser, last_login=now,
        date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, False, False,
        **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user

def upload_location1 (instance,filename):
    return "accounts/avatars/%s/%s" %(instance.id, filename)

def upload_location2 (instance,filename):
    return 'accounts/picresume/user_{0}/user_{0}_{1}'.format(instance.user.id, filename) #"accounts/picresume/user_%s/%s" %(instance.user.id ,filename)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=15,
    help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
    validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
     _('Enter a valid username.'), _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    birth_date = models.CharField(_('birth date'),max_length=10,null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
      help_text=_('Designates whether the user can log into this admin site.'))
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(default='accounts/defaults/default1.jpg', upload_to=upload_location1) #, blank=True) # null=True)
    picresume = models.ImageField( default='accounts/defaults/default1.jpg', upload_to=upload_location2 ) #, blank=True , null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','birth_date']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        #Returns the first_name plus the last_name, with a space in between.
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        #Returns the short name for the user.
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        #Sends an email to this User.
        send_mail(subject, message, from_email, [self.email], **kwargs)

    #Resize Image Install Pillow
    def save(self,**kwargs):
        super().save()
        img1 = Image.open(self.avatar.path)
        img2 = Image.open(self.picresume.path)

        if img1.height > 300 or img1.width > 300:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.avatar.path)

        if img2.height > 300 or img2.width > 300:
            output_size = (300,300)
            img2.thumbnail(output_size)
            img2.save(self.picresume.path)


class Profile(models.Model): 
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imageresume = models.ImageField(default='accounts/defaults/default1.jpg',
     upload_to=upload_location2)

    #Name + profile
    def __str__(self):
        return f'{self.user.username} Profile'

    #Resize Image Install Pillow
    def save(self,**kwargs):
        super().save()
        img1 = Image.open(self.imageresume.path)

        if img1.height > 300 or img1.width > 300:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.imageresume.path)


#it will create Profile then User will create 
@receiver(signals.post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
