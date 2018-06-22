from __future__ import unicode_literals

import re
import string

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import PPOIField, VersatileImageField


def random_id():
    unique_id = get_random_string(
        length=12, allowed_chars='01234567-89qwertyuiopasdfghjklzxcvbnm')
    return unique_id


def upload_profile_location(instance, filename, *args, **kwargs):
    location = random_id()
    return "media/profile-images/%s/%s" % (location, filename)


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser,
                     first_name, last_name, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, first_name, last_name,
                    **extra_fields):
        if len(first_name) > 1:
            first_name = first_name[0].upper() + first_name[1:]
        if len(last_name) > 1:
            last_name = last_name[0].upper() + last_name[1:]

        return self._create_user(username, email, password, False, False, first_name, last_name, **extra_fields)

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self._create_user(
            username, email, password, True, True, first_name, last_name)
        user.is_active = True
        user.save(using=self._db)
        return user


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

MEMBERSHIP_LEVELS = (

    ('full_membership', 'Dependant Spouse'),
    ('full_membership', 'Legacy Membership'),
    ('full_membership', 'Full Membership (Family)'),
    ('full_membership', 'Full Membership (Individual)'),
    ('national_membership', 'Jr. National Membership'),
    ('national_membership', 'National Membership'),
    ('senior_membership', 'Senior (Family)'),
    ('senior_membership', 'Senior (Individual)'),
    ('social_membership', 'Social Membership'),
    ('senior_membership', 'TBCC Senior (Family)'),
    ('senior_membership', 'TBCC Senior (Individual)'),
    ('weekday_membership', 'TBCC Senior (Weekday)'),
    ('weekday_membership', 'Weekday (Individual)'),
    ('weekday_membership', 'Weekday (Senior)'),
    ('young_executive_membership', 'Young Executive (21-32)'),
    ('young_executive_membership', 'Young Executive (33-39)'),
    ('young_executive_membership', 'Young Executive (40-45)')

)


NAME_SUFFIX = (  # Used several common name suffixes
    ('CPA', 'CPA'),
    ('Esq', 'Esq.'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('JD', 'JD'),
    ('Jr.', 'Jr.'),
    ('M.D.', 'M.D.'),
    ('Ph. D.', 'Ph. D.'),
    ('Sr.', 'Sr.'),
    ('USA', 'USA'),
    ('USAF', 'USAF'),
    ('USAFR', 'USAFR'),
    ('USAR', 'USAR'),
    ('USCG', 'USCG'),
    ('USMC', 'USMC'),
    ('USMCR', 'USMCR'),
    ('USN', 'USN'),
    ('USNR', 'USNR'),

)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_index=True,
        verbose_name='Username',
        unique=True,
        max_length=255,
        help_text=_(
            'Required. 255 characters or fewer. Letters, numbers and \
            @/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username.'),
                _('invalid')
            )
        ]
    )
    email = models.EmailField(
        db_index=True,
        verbose_name='Email',
        unique=True,
        max_length=255
    )
    member_code = models.CharField(
        verbose_name='Member Code',
        max_length=60,
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=60
    )
    middle_name = models.CharField(
        verbose_name='Middle Name',
        max_length=60,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=60
    )

    profile_image = VersatileImageField(
        'Profile Image',
        upload_to=upload_profile_location,
        ppoi_field='ppoi',
        blank=True,
        null=True,
    )
    ppoi = PPOIField(
        'Image PPOI',
        default=(0.5, 0.5),
    )
    phone_numner = models.CharField(
        blank=True,
        verbose_name='Phone Number',
        max_length=60,
    )
    e_contact_full_name = models.CharField(
        blank=True,
        verbose_name='Emergency Contact Full Name',
        max_length=60,
    )
    e_contact_phone_number = models.CharField(
        blank=True,
        verbose_name='Emergency Contact Phone Number',
        max_length=60
    )
    is_active = models.BooleanField(
        verbose_name='Active User',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff User',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='Updated At',
        auto_now=True
    )
    gender = models.CharField(
        'Gender',
        max_length=120,
        choices=GENDER,
        blank=True,
        default="",
    )
    suffix = models.CharField(
        'Name Suffix',
        max_length=120,
        blank=True,
        choices=NAME_SUFFIX,
        default="",
    )
    membership_level = models.CharField(
        'Membership Level',
        max_length=120,
        # choices=MEMBERSHIP_LEVELS,
        blank=True
    )
    needs_to_be_put_into_event_man = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __unicode__(self):
        return smart_text(self.first_name + ' ' + self.last_name)

    class Meta:
        verbose_name = 'WVGC Site User'
        verbose_name_plural = 'WVGC Site Users'

    def get_full_name(self):
        middle_name = ''
        suffix = ''
        if self.middle_name is not None:
            middle_name = ' ' + str(self.middle_name)
        if self.suffix is not None:
            suffix = self.suffix
        full_name = '%s%s %s %s' % (
            self.first_name, middle_name, self.last_name, suffix)
        return full_name.rstrip()

    def get_member_code(self):
        return str(self.member_code)

    def get_short_name(self):
        short_name = '%s %s' % (self.first_name, self.last_name)
        return short_name.rstrip()

    def get_profile_image(self):
        try:
            cropped_image = self.profile_image.crop['300x300']
            return cropped_image.url
        except:
            return 'https://www.watchungvalleygc.com/static/img/WVGC-Logo.50359d99df57.svg'

    def get_clean_phonenumber(self):
        if self.phone_numner:
            phonenumber = self.phone_numner

            return re.sub("\D", "", phonenumber)

        else:
            pass

# method for updating


@receiver(post_save, sender=User)
def update_cache(sender, instance, **kwargs):
    members = User.objects.all().order_by('last_name').exclude(is_staff=True)
    cache.clear()
    cache.set('members', members, 600)
    print 'CACHE UDPATED'


class UserPhoneNumber(models.Model):
    phone_numner = models.CharField(
        blank=True,
        verbose_name='Phone Number',
        max_length=60,
    )
    member_code = models.CharField(
        blank=True,
        verbose_name='Member Code',
        max_length=60,
    )

    def __unicode__(self):
        return str(self.id)
