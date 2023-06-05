import os
import uuid
# import boto3
from django.shortcuts import render
# from .models import Owl, Photo



# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the main_app index.")

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'nightowl/login.html')

def about(request):
    return render(request, 'about.html')

# def add_photo(request, owl_id):
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         try: 
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             Photo.objects.create(url=url, owl_id=owl_id)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
#     return redirect('detail', owl_id=owl_id)
