import logging
from custom_logger import EmailNotificationHandler
from samapp.models import management_group, model_category, model_manufacturer, asset_model
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

def my_view(request):
    logger = logging.getLogger(__name__)

    # Log an error message
    logger.error('An error occurred while updating the asset.')

    # ...

    return HttpResponse('...')