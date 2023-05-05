from samapp.models import asset, management_group, business_unit, model_category, asset_model
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

def homepage(request):
    models = asset_model.AssetModel.objects.all().distinct()
    business_units = business_unit.BusinessUnit.objects.all()
    assets = asset.Asset.objects.all()
    
    context = {
            "assets": assets,
            "models": models,
            "business_units": business_units
        }
    return render(request, "homepage.html", context)