from django.db import models
from bitfield import BitField

# Create your models here.
class Student(models.Model):
    personal_info = BitField(flags=(
        ('is_graduated', 'Graduated'),
        ('is_male', 'Is male'),
        ('apply_scolarship', 'Applied scolarship')
    ))