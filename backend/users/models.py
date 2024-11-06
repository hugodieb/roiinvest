from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re

def validate_cpf(value):
  if not re.match(r'^\d{11}$', value):
    raise ValidationError('CPF deve conter 11 dígitos numéricos.')


class User(AbstractUser):
  SUBSCRIPTION_CHOICES = [
    ('free', 'Free'),
    ('pro', 'Pro'),
    ('super_pro', 'Super Pro'),
    ('admin', 'Admin'),
  ]

  subscription_type = models.CharField(
    max_length=10,
    choices=SUBSCRIPTION_CHOICES, default='free'
  )
  email = models.EmailField(unique=True

  def __str__(self):
    return self.email                            
)
  
class Profile(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='profile'
  )
  birth_date = models.DateField()
  age = models.IntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(150)]
  )
  cpf = models.CharField(
    max_length=11,
    unique=True,
    validators=[validate_cpf]
  )
  phone = models.CharField(
    max_length=15
  )
  avatar = models.ImageField(
    upload_to='avatars/',
    null=True,
    blank=True
  )

  def clean(self):
    super().clean()
  
  def __str__(self):
    return self.user.email