
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from .serializer import *
from . forms import *

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.views.generic import *
from rest_framework import generics, filters,status
# Create your views here.


@login_required(login_url='/loginfunc')
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

    

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MyEventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(user=self.request.user.id)
        return queryset

# Retrieves details of a Event
class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



@api_view(['POST'])
def eventlike(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    liked_event, created = LikedEvent.objects.get_or_create(user=request.user, event=event)
    if created or not liked_event.is_liked:
        liked_event.is_liked = True
        # event.likes_count += 1
    else:
        liked_event.is_liked = False
        # event.likes_count -= 1
    liked_event.save()
    event.save()
    return Response({
        'id': event.id,
        'is_liked': liked_event.is_liked,
        'likes_count': event.likes_count,
    }, status=status.HTTP_200_OK)



# =========================================


def loginfunc(request):  
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f' welcome!')
            return redirect('/')
        else:
            messages.info(request, 'Email/Password incorrect')
            return redirect('loginfunc')
    return render (request, 'frontend/login.html')

def logoutfunc(request):
    logout(request)
    return redirect('loginfunc')


def registerfunc(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print('here')
            new_user = form.save(commit=False)
            new_user.save()
            login(request, new_user)
            messages.success(request, 'Signup Successful!')
            return redirect('/myevents') 
        else:
            messages.error(request, form.errors)
            return redirect('registerfunc')
    return render(request, 'frontend/register.html')
