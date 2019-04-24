from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

import hashlib

# Create your models here.

class Account(AbstractUser):
    pass

# instance is the Profile object
# filename is the original filename
def image_upload_to(instance, filename):
    # dont let the user-provided filename influence anything
    filename = None

    try:
        # get the users' username
        username = instance.accountid.username
        username_bytes = username.encode('utf-8')
        username_hash = hashlib.sha256(username_bytes).hexdigest()

    except:
        filename = instance.name
        filename_bytes = filename.encode('utf-8')
        username_hash = hashlib.sha256(filename_bytes).hexdigest()

    return 'images/{}.jpg'.format(username_hash)

class Profile(models.Model):

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    ROLE_MENTOR = 'TOR'
    ROLE_MENTEE = 'TEE'
    ROLE_CHOICES = (
        (ROLE_MENTOR, 'Mentor'),
        (ROLE_MENTEE, 'Mentee')
    )

    image = models.FileField(upload_to=image_upload_to, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    birthdate = models.DateField(null=True)
    givenname = models.CharField(max_length=32)
    familyname = models.CharField(max_length=32)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default=ROLE_MENTEE)
    job = models.CharField(max_length=32, null=True)
    about = models.TextField(max_length=1024, null=True)
    city = models.CharField(max_length=32, null=True)
    accountid = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null = True
    )
    subjects = models.ManyToManyField('Subject', related_name='subjects_users')

    def __str__(self):
        return "{}, {} ({})".format(self.familyname, self.givenname, str(self.id))

class Subject(models.Model):

    CATEGORY_ACADEMIC = 'AC'
    CATEGORY_LANG = 'LANG'
    CATEGORY_INSTR = 'I'
    CATEGORY_ARTS = 'AR'
    CATEGORY_HANDF = 'HANDF'
    CATEGORY_PROF = 'P'
    CATEGORY_LS = 'L'
    CATEGORY_CHOICES = (
        (CATEGORY_ACADEMIC, 'Academic'),
        (CATEGORY_LANG, 'Language'),
        (CATEGORY_INSTR, 'Musical Instruments'),
        (CATEGORY_ARTS, 'Arts'),
        (CATEGORY_HANDF, 'Health and Fitness'),
        (CATEGORY_PROF, 'Professional'),
        (CATEGORY_LS, 'Lifestyle')
    )

    name = models.TextField(max_length=32)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default=CATEGORY_LS)

# Profile messages
class Message(models.Model):
    sender = models.ForeignKey(
        Profile,
        related_name = "message_sender",
        on_delete=models.SET_NULL,
        null = True
    )
    receiver = models.ForeignKey(
        Profile,
        related_name = "message_receiver",
        on_delete=models.SET_NULL,
        null = True
    )
    content = models.TextField(max_length=1024)
    timestamp_sent = models.DateTimeField(auto_now_add=True)
    timestamp_read = models.DateTimeField(auto_now_add=False, null = True, blank = True)
    public = models.BooleanField(default=False)

class Event(models.Model):
    image = models.FileField(upload_to=image_upload_to)
    date = models.DateField()
    time = models.TimeField()
    public = models.BooleanField(default=True)
    name = models.CharField(max_length=32)
    about = models.TextField(max_length=1024, null=True)
    host = models.ForeignKey(
        Profile,
        related_name = "host_of_event",
        on_delete=models.SET_NULL,
        null = True
    )
    location = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    subjects = models.ManyToManyField('Subject', related_name='subjects_events')
    attendees = models.ManyToManyField('Profile', related_name='a_profiles_events')
    invitees = models.ManyToManyField('Profile', related_name='i_profiles_events')

    def event_id(self):
        return self.id
