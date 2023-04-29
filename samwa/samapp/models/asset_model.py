from django.db import models
from django.utils.translation import gettext_lazy as _
from . import model_category, model_manufacturer

class AssetModel(models.Model):
    """
    Model representing the asset model.
    """
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    category = models.ForeignKey(model_category.ModelCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    number = models.CharField(max_length=10, verbose_name="Number")
    manufacturer = models.ForeignKey(model_manufacturer.ModelManufacturer, on_delete=models.CASCADE, verbose_name=_('Manufacturer'))

    def __str__(self):
        return f"{self.name} [{self.number}]"
    
    class Meta:
        verbose_name = _('Asset Model')
        verbose_name_plural = _('Asset Models')