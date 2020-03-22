from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('academic/<int:pk>/',views.delete2,name='delete2'),
    path('academic/responses_view/<int:pk>/',views.delete3,name='delete3'),
    path('academic/responses_view/innovation/<int:pk>/',views.delete4,name='delete4'),
    path('academic/responses_view/UG/<int:pk>/',views.delete5,name='delete5'),
    path('academic/responses_view/PG/<int:pk>/',views.delete6,name='delete6'),
    path('academic/responses_view/ExtraCurricular/<int:pk>/',views.delete7,name='delete7'),
    path('academic/responses_view/AllClear/<int:pk>/',views.delete8,name='delete8'),
    path('academic/responses_view/ThreeClear/<int:pk>/',views.delete9,name='delete9'),
    path('academic/responses_view/Article/<int:pk>/',views.delete10,name='delete10'),
    path('academic/responses_view/Competitive/<int:pk>/',views.delete11,name='delete11'),
    path('academic/responses_view/Startups/<int:pk>/',views.delete12,name='delete12'),
    path('academic/responses_view/Awards/<int:pk>/',views.delete13,name='delete13'),
    path('academic/responses_view/Prizes/<int:pk>/',views.delete14,name='delete14'),
    path('academic/responses_view/Internship/<int:pk>/',views.delete15,name='delete15'),
    path('academic/responses_view/OnlineCertification/<int:pk>/',views.delete16,name='delete16'),



    path('academic/',views.AcademicView.as_view(),name='academic'),
    
    path('academic/academics_list/',views.AcadListView.as_view(),name='academics_list'),
    path('academic/academics_list/<str:user>/<int:pk>',views.FacAcadListView.as_view(),name='fac_acad'),

    path('academic/responses_view/',views.ResponsesView.as_view(),name='responses_view'),
]