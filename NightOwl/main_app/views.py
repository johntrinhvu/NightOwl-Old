# import os
# import uuid
# import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event




# Create your views here.
from django.http import HttpResponse

events = [
  {'name': 'Toga Party', 'description': 'Rager at secret location strict dress code, 21+ only', 'location': 'Los Angeles, CA', 'date': '06/08/2023', 'capacity': 'Capacity 88/150'},
  {'name': 'Jazz Function', 'description': '21+ only', 'location': 'Hollywood, CA', 'date': '06/08/2023', 'capacity': 'Capacity 13/25'},
]

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'type', 'location', 'time', 'capacity', 'restrictions', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def index(request):
    return HttpResponse("Hello, world. You're at the main_app index.")

def home(request):
    return render(request, 'home.html')

def events_index(request):
    return render(request, 'events/index.html', {
        'events': events
    })

def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'

    return render(request, 'nightowl/login.html', {'error_message': error_message})

def about(request):
    return render(request, 'about.html')

# @login_required
# def add_photo(request, event_id):
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         try: 
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             Photo.objects.create(url=url, event_id=event_id)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
#     return redirect('detail', event_id=event_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'nightowl/login.html', context)


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
