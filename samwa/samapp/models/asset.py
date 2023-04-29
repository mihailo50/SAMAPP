from django.db import models
from django.utils.translation import gettext_lazy as _

from .  import asset_model, business_unit



class Asset(models.Model):
    """
    Model representing an asset.
    """
    name = models.CharField(max_length=15, verbose_name=_('Name'))
    model = models.ForeignKey(asset_model.AssetModel, on_delete=models.CASCADE, verbose_name=_('Model'), related_name='models')
    warranty = models.DateField(verbose_name=_('Warranty'))
    business_unit = models.ForeignKey(business_unit.BusinessUnit, on_delete=models.CASCADE, verbose_name=_('Business Unit'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    order_number = models.CharField(max_length=10, verbose_name=_('Order Number'))
    STATUS_CHOICES = [
        ('deployed', _('Deployed')),
        ('in_storage', _('In Storage')),
        ('ready_for_deployment', _('Ready for Deployment')),
        ('malfunction', _('Malfunction')),
        ('recycled', _('Recycled')),
        ('ready_for_recycle', _('Ready for Recycle')),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=_('Status'))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('Asset')
        verbose_name_plural = _('Assets')

    def save(self, *args, **kwargs):
        if not self.warranty:
            self.warranty = self.model.warranty
        super().save(*args, **kwargs)