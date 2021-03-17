from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.AcademicView.as_view(),name='research'),
   path('fac_list/',views.AcadListView.as_view(),name='academics_list3'),
    path('fac_list/<str:user>/<int:pk>',views.FacAcadListView.as_view(),name='fac_acad3'),

    path('responses_view/',views.ResponsesView.as_view(),name='responses_view3'),



    path('<int:pk>/',views.delete2,name='redelete2'),
    path('responses_view/<int:pk>/',views.delete3,name='redelete3'),
    path('responses_view/innovation/<int:pk>/',views.delete4,name='redelete4'),
    path('responses_view/UG/<int:pk>/',views.delete5,name='redelete5'),
    path('responses_view/PG/<int:pk>/',views.delete6,name='redelete6'),
    path('responses_view/ExtraCurricular/<int:pk>/',views.delete7,name='redelete7'),
    path('responses_view/AllClear/<int:pk>/',views.delete8,name='redelete8'),
    path('responses_view/ThreeClear/<int:pk>/',views.delete9,name='redelete9'),
    path('responses_view/Article/<int:pk>/',views.delete10,name='redelete10'),
    path('responses_view/Competitive/<int:pk>/',views.delete11,name='redelete11'),
    path('responses_view/Startups/<int:pk>/',views.delete12,name='redelete12'),
    path('responses_view/Awards/<int:pk>/',views.delete13,name='redelete13'),
    path('responses_view/Prizes/<int:pk>/',views.delete14,name='redelete14'),
    path('responses_view/Internship/<int:pk>/',views.delete15,name='redelete15'),
    path('responses_view/Internship/<int:pk>/',views.delete15,name='redelete16'),
   
]