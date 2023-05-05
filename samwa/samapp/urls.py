from django.urls import path
from samapp.views import assets, homepage, extract, users

urlpatterns = [
    path('homepage/', homepage.homepage, name="homepage"),
    path('all_assets/', assets.all_assets, name="all_assets"),
    path('asset/<int:id>/', assets.asset_details, name='asset_details'),

    # login
    path('', users.login, name="login"),

    # extract
    path('assets/excel', extract.extract_all_excel, name="extract_all_excel"),
    path('asssets/json', extract.extract_all_json, name="extract_all_json"),

    # menu
    path('filter/', assets.filter_menu, name="filter_menu"),
    path('assets/', assets.asset_menu, name="asset_menu"),
    
    # filter
    # path('filter_by_model/', assets.filter_by_model, name='filter_by_model'),
    # path('filter_by_price/', assets.filter_by_price_range, name='filter_by_price_range'),
    # path('filter_by_bu/', assets.filter_by_bu, name="filter_by_bu"),
    path('filter/assets', assets.filter_assets, name="filter_assets"),
    path('search/', assets.search_asset, name="search_asset"),


    # manage
    path('create_asset/', assets.create_asset, name="create_asset"),
    path('update_asset/<int:id>/', assets.update_asset, name="update_asset"),
    path('remove_asset/<int:id>/', assets.remove_asset, name='remove_asset')
]