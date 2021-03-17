from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('profile/<int:pk>/',views.delete,name='delete'),
    path('profile/prof/',views.ProfileList.as_view(),name='prof'),
    path('profile/prof/<str:user>/',views.UserProfile.as_view(),name='user_prof'),
    path('api-list/',views.APIview.as_view(),name='api_list'),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)