from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('asesor', 'Asesor'),
        ('cliente', 'Cliente'),
    )

    rol = models.CharField(max_length=15, choices=ROLE_CHOICES)

    class Meta:
        managed = False
