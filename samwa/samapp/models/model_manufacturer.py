from django.db import models
from django.utils.translation import gettext_lazy as _

class ModelManufacturer(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('Name'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')