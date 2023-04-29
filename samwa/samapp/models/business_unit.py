from django.db import models
from django.utils.translation import gettext_lazy as _

from .management_group import ManagementGroup


class BusinessUnit(models.Model):
    """
    Model representing a business unit.
    """
    short_name = models.CharField(max_length=7, verbose_name=_('Short Name'))
    full_name = models.CharField(max_length=20, verbose_name=_('Full Name'))
    management_group = models.ForeignKey(ManagementGroup, on_delete=models.CASCADE, verbose_name=_('Management Group'))

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _('Business Unit')
        verbose_name_plural = _('Business Units')
