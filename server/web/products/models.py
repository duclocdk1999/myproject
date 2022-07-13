from django.db import models

# Create your models here.
class Accessory(models.Model):
    """
    This model is used to store motorbike accessories information
    """
    system_name = models.CharField(max_length=100, null=False)
    unicode_name = models.CharField(verbose_name='tên sản phẩm', max_length=100, blank=False)

    class Meta:
        verbose_name_plural = 'Accessories'
    

class Vehicle(models.Model):
    """
    This model is used to store motorbike information
    """

    class Meta:
        verbose_name_plural = 'Vehicles'