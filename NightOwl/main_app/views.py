import os
import uuid
import boto3
from django.shortcuts import render
from .models import Owl, Photo



# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the main_app index.")