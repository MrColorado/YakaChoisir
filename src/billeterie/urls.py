"""billeterie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf.urls.static import static


from billeterie import settings
from database.views import event_views
from database.views import home_views
from database.views import user_views
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('user_settings/', user_views.user_information, name='settings'),

    path('event/', event_views.event, name='event'),
    path('create_event/', event_views.create_event, name='create_event'),
    path('event/<int:event_id>/', event_views.specific_event, name='specific_event'),
    path('register/<int:current_event>/', event_views.register, name='register'),
    path('my_event/', event_views.my_event, name='my_event'),

    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

