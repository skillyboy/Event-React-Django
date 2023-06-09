from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('logoutfunc', logoutfunc, name='logoutfunc'),
    
    path('loginfunc', loginfunc, name='loginfunc'),
    path('registerfunc', registerfunc, name='registerfunc'),
    
    path('events', index, name='events'),
    path('myevents/', index, name='myevents'),
    
    path('event/<int:pk>', EventDetail.as_view(), name='create-event'),
    
    path('eventslist/', EventListView.as_view(), name='event_list'),
    path('myeventslist/', MyEventListView.as_view(), name='my_event_list'),
   
    path('event/create', EventCreateView.as_view()),

    path('event/<int:event_id>/like', eventlike),
]
