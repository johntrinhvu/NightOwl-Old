import os
import uuid
import boto3
from django.shortcuts import render
from .models import Event, Photo

# Create your views here.
from django.http import HttpResponse

events = [
  {'name': 'Toga Party', 'description': 'Rager at secret location strict dress code, 21+ only', 'location': 'Los Angeles, CA', 'date': '06/08/2023', 'capacity': 'Capacity 88/150'},
  {'name': 'Jazz Function', 'description': '21+ only', 'location': 'Hollywood, CA', 'date': '06/08/2023', 'capacity': 'Capacity 13/25'},
]

def events_index(request):
    return render(request, 'events/index.html', {
        'events': events
    })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_photo(request, event_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try: 
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, event_id=event_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', event_id=event_id)
