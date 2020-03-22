from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.AcademicView.as_view(),name='research'),
   path('fac_list/',views.AcadListView.as_view(),name='academics_list3'),
    path('fac_list/<str:user>/<int:pk>',views.FacAcadListView.as_view(),name='fac_acad3'),

    path('responses_view/',views.ResponsesView.as_view(),name='responses_view3'),



    path('<int:pk>/',views.delete2,name='delete2'),
    path('responses_view/<int:pk>/',views.delete3,name='delete3'),
    path('responses_view/innovation/<int:pk>/',views.delete4,name='delete4'),
    path('responses_view/UG/<int:pk>/',views.delete5,name='delete5'),
    path('responses_view/PG/<int:pk>/',views.delete6,name='delete6'),
    path('responses_view/ExtraCurricular/<int:pk>/',views.delete7,name='delete7'),
    path('responses_view/AllClear/<int:pk>/',views.delete8,name='delete8'),
    path('responses_view/ThreeClear/<int:pk>/',views.delete9,name='delete9'),
    path('responses_view/Article/<int:pk>/',views.delete10,name='delete10'),
    path('responses_view/Competitive/<int:pk>/',views.delete11,name='delete11'),
    path('responses_view/Startups/<int:pk>/',views.delete12,name='delete12'),
    path('responses_view/Awards/<int:pk>/',views.delete13,name='delete13'),
    path('responses_view/Prizes/<int:pk>/',views.delete14,name='delete14'),
    path('responses_view/Internship/<int:pk>/',views.delete15,name='delete15'),
    path('responses_view/Internship/<int:pk>/',views.delete15,name='delete16'),
   
]