from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from samapp.models import management_group, model_category, model_manufacturer, asset_model
from samapp.models.asset import Asset
from samapp.models.business_unit import BusinessUnit
from django.contrib import messages


def get_asset(asset_id):
    """
    Retrieve an asset object from the database based on the given asset_id.
    """
    try:
        asset = asset.Asset.objects.get(id=asset_id)
        return asset
    except asset.Asset.DoesNotExist:
        return None

def update_database(asset):
    """
    Save the updated asset object to the database.
    """
    asset.save()


# list all
def all_assets(request):
    business_units = BusinessUnit.objects.all()
    assets = Asset.objects.all()
    categories = model_category.ModelCategory.objects.all()
    success_messages = messages.get_messages(request)

    context = {
        "assets": assets,
        "business_units": business_units,
        "categories": categories,
        'success_messages': success_messages,
    }
    return render(request, "assets/all_assets.html", context)


def asset_details(request, id):
    asset_detail = get_object_or_404(Asset, id=id)
    status_choices = dict(asset_detail.STATUS_CHOICES)
    context = {
        "asset": asset_detail,
        "status_choices": status_choices,
    }
    return render(request, "assets/asset.html", context)


# manage assets

def filter_menu(request):
    models = asset_model.AssetModel.objects.all()
    bu = BusinessUnit.objects.all()
    context = {
        "models": models,
        "business_units": bu,
    }
    return render(request, "menu/filter_menu.html", context)

def asset_menu(request):
    assets = Asset.objects.all()
    context = {
        "assets": assets,
    }
    return render(request, "menu/asset_menu.html", context)

def filter_by_model(request):
    if request.method == 'POST':
        selected_model_id = request.POST.get('selected_model')
        if selected_model_id:
            assets = Asset.objects.filter(model__id=selected_model_id)
        else:
            assets = Asset.objects.all()
        context = {
            "assets": assets,
        }
        return render(request, 'assets/all_assets.html', context)

    
def filter_by_price_range(request):
    if request.method == "POST":
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price is not None and max_price is not None or min_price != "" and max_price != "":
            assets = Asset.objects.filter(price__gte=min_price, price__lte=max_price)
            context = {
            'assets': assets,
            'min_price': min_price,
            'max_price': max_price
            }
            return render(request, 'assets/filtered_assets.html', context)
        else:
            assets = Asset.objects.all()
        context = {
            'assets': assets,
            'min_price': min_price,
            'max_price': max_price,
        }
        return render(request, 'assets/filtered_assets.html', context)
    
def filter_by_bu(request):
    bu = BusinessUnit.objects.all()
    if request.method == 'POST':
        selected_bu = request.POST.get('selected_bu')
        assets = Asset.objects.filter(model__id=selected_bu)
        context = {
            "assets": assets,
            "business_units": bu,
        }
        return render(request, 'assets/all_assets.html', context)
    else:
        print("FILTER GET")
        context = {
            "models": bu,
        }
        return render(request, 'assets/filtered_assets.html', context)


def create_asset(request):
    asset_models = asset_model.AssetModel.objects.all()
    business_units = BusinessUnit.objects.all()
    status_choices = Asset.STATUS_CHOICES
    print(business_units)
    context = {
        "models": asset_models,
        "status_choices": status_choices,
        "business_units": business_units
    }
    if request.method == "GET":
        return render(request, "assets/create_asset.html", context)
    if request.method == 'POST':
        new_asset = Asset()
        new_asset.name = request.POST.get('name')
        new_asset.model = asset_model.AssetModel.objects.get(pk=request.POST['model'])
        new_asset.warranty = request.POST.get('warranty')
        new_asset.business_unit = BusinessUnit.objects.get(pk=request.POST['business_unit'])
        new_asset.price = request.POST.get('price')
        new_asset.order_number = request.POST.get('order_number')
        new_asset.status = request.POST.get('status')
        print("-------",new_asset)
        
        new_asset.save()
        
        return redirect('all_assets')





def update_asset(request, id):
    """
    Update asset.
    """
    asset = get_object_or_404(Asset, id=id)
    models = asset_model.AssetModel.objects.all()
    management_groups = management_group.ManagementGroup.objects.all()
    if request.method == "GET":
        print("UPDATE ASSET ID:  ",asset)
        context = {
            "asset": asset,
            "models": models,
            "management_groups": management_groups,
        }
        return render(request, "assets/manage/update_asset.html", context)
    if request.method == "POST":
        asset.name = request.POST['name']
        asset.price = request.POST['price']
        asset.order_number = request.POST['order_number']
        asset.warranty = request.POST['warranty']
        asset.model = asset_model.AssetModel.objects.get(pk=request.POST['model'])
        asset.category = model_category.ModelCategory.objects.get(pk=request.POST['category'])
        asset.status = request.POST['status']
        asset.save()




def remove_asset(request, id):
    selected_asset = get_object_or_404(Asset, id=id)
    assets = Asset.objects.all()
    context = {
        "assets": assets,
    }
    selected_asset.delete()
    return render(request, "assets/all_assets.html", context)

