from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from social_media_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # root -> /overview/ এ রিডাইরেক্ট
    path('', RedirectView.as_view(pattern_name='overview', permanent=False)),

    path('home/', views.home, name='home'),
    path('overview/', views.overview, name='overview'),
]
