from django.contrib import admin
from .models import asset, asset_model, management_group, business_unit, model_category, model_manufacturer
# Register your models here.
admin.site.register(asset.Asset)
admin.site.register(management_group.ManagementGroup)
admin.site.register(business_unit.BusinessUnit)
admin.site.register(asset_model.AssetModel)
admin.site.register(model_category.ModelCategory)
admin.site.register(model_manufacturer.ModelManufacturer)