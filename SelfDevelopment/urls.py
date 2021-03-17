from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.SelfDevelopment.as_view(),name='selfdevelopment'),
   path('fac_list/',views.AcadListView.as_view(),name='academics_list2'),
    path('fac_list/<str:user>/<int:pk>',views.FacAcadListView.as_view(),name='fac_acad2'),

    path('responses_view/',views.ResponsesView.as_view(),name='responses_view2'),


    path('<int:pk>/',views.delete2,name='sddelete2'),
    path('responses_view/<int:pk>/',views.delete3,name='sddelete3'),
    path('responses_view/innovation/<int:pk>/',views.delete4,name='sddelete4'),
    path('responses_view/UG/<int:pk>/',views.delete5,name='sddelete5'),
    path('responses_view/PG/<int:pk>/',views.delete6,name='sddelete6'),
    path('responses_view/ExtraCurricular/<int:pk>/',views.delete7,name='sddelete7'),
    path('responses_view/AllClear/<int:pk>/',views.delete8,name='sddelete8'),
    path('responses_view/ThreeClear/<int:pk>/',views.delete9,name='sddelete9'),
    path('responses_view/Article/<int:pk>/',views.delete10,name='sddelete10'),
    path('responses_view/Competitive/<int:pk>/',views.delete11,name='sddelete11'),
    path('responses_view/Startups/<int:pk>/',views.delete12,name='sddelete12'),
    path('responses_view/Awards/<int:pk>/',views.delete13,name='sddelete13'),
    path('responses_view/Prizes/<int:pk>/',views.delete14,name='sddelete14'),
    path('responses_view/Internship/<int:pk>/',views.delete15,name='sddelete15'),
   
]