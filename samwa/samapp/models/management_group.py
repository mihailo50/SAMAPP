from django.db import models
from django.utils.translation import gettext_lazy as _


class ManagementGroup(models.Model):
    """
    Model representing the management group of an asset.
    """
    name = models.CharField(max_length=20, verbose_name=_('Name'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Management Group')
        verbose_name_plural = _('Management Groups')