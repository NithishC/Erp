from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.EventsView.as_view(),name='events'),
    path('<int:pk>/',views.delete2,name='delete2'),
    path('events_responses_view/<int:pk>/',views.delete3,name='delete3'),
    path('events_responses_view/national_conf/<int:pk>/',views.delete4,name='delete4'),
    path('events_responses_view/workshop/<int:pk>/',views.delete5,name='delete5'),
    path('events_responses_view/fdp/<int:pk>/',views.delete6,name='delete6'),
    path('events_responses_view/inter_college/<int:pk>/',views.delete7,name='delete7'),
    path('events_responses_view/international_conf2/<int:pk>/',views.delete8,name='delete8'),
    path('events_responses_view/national_conf2/<int:pk>/',views.delete9,name='delete9'),
    path('events_responses_view/workshop2/<int:pk>/',views.delete10,name='delete10'),
    path('events_responses_view/fdp2/<int:pk>/',views.delete11,name='delete11'),
    path('events_responses_view/inter_college2/<int:pk>/',views.delete12,name='delete12'),
    path('events_responses_view/',views.ResponsesView.as_view(),name='events_responses_view'),
    path('events_list/',views.EventsList.as_view(),name='events_list'),
    path('events_list/<str:user>/<int:pk>',views.FacEventsList.as_view(),name='fac_events'),

]
