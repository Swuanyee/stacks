"""users/models.py"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GROUP_CHOICES = (
        ('Sec 1', 'Sec 1'),
        ('Sec 2', 'Sec 2'),
        ('Sec 3', 'Sec 3'),
        ('Sec 4', 'Sec 4'),
        ('J1', 'J1'),
        ('J2', 'J2'),
        ('Public', 'Public'),
        ('Teacher', 'Teacher'),
    )
    """username was changed to email"""
    first_name = models.CharField(blank=False, unique=False,
                                  max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, unique=False,
                                 max_length=150, verbose_name='last name')
    username = models.CharField(max_length=30, unique=False)
    profile = models.CharField(
            blank=False,
            max_length=100,
            choices=GROUP_CHOICES,
            default='Public')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
