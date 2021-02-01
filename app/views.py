from django.shortcuts import render, HttpResponse
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.info('index - page')
    return HttpResponse('<b>Hello Word</b>')
