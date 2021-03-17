from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.ContributionsView.as_view(),name='contribs'),
    path('contribs_responses_view/',views.ResponsesView.as_view(),name='contribs_responses_view'),
    path('contribs_list/',views.ContribsList.as_view(),name='contribs_list'),
    path('contribs_list/<str:user>/<int:pk>',views.FacContribsList.as_view(),name='fac_contribs'),
    path('<int:pk>/',views.delete2,name='delete2'),
    path('contribs_responses_view/<int:pk>/',views.delete3,name='delete3'),
    path('contribs_responses_view/national_conf/<int:pk>/',views.delete4,name='delete4'),
]
