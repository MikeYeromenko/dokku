from django.shortcuts import render
from django.http import HttpResponse

from dokkutest.celery import print_task

# Create your views here.

def index(request):
    # text = print_task.delay()
    text = 'Celery doesn\'t work:('
    return HttpResponse(content=f'Works!: request.path - {request.path}. Celery text: {text}.')