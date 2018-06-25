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
from tastypie.api import Api

from billeterie import settings
from database.views import event_views
from database.views import home_views
from database.views import association_views
from database.views import user_views
from django.contrib.auth import views
from database.views import paypal_view
from database.views import base_views

from api.resources import *

api = Api(api_name='v1')

api.register(MembersResource())
api.register(EventMembersResource())
api.register(EventsResource())
api.register(UsersResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('base/', base_views.search, name='search'),
    path('user_settings/', user_views.user_information, name='settings'),
    path('user_settings/modification', user_views.user_modify, name='user_modify'),
    path('user_settings/stat', user_views.stat, name='stat'),

    path('evenements/', event_views.event, name='event'),
    path('creation_evenement/', event_views.create_event, name='create_event'),
    path('change_event/<int:event_id>/', event_views.modify_event, name='modify_event'),
    path('evenements/<int:event_id>/', event_views.specific_event, name='specific_event'),
    path('inscription/<int:current_event>/', event_views.register, name='register'),
    path('inscription_after_pay/<int:current_event>/', event_views.register_after_pay,
         name='register_after_pay'),
    path('mes_evenements/', event_views.my_event, name='my_event'),

    path('associations/', association_views.association, name='association'),
    path('creation_association/', association_views.create_association, name='create_association'),
    path('association/<int:asso_id>/', association_views.specific_association, name='specific_association'),
    path('association/<int:asso_id>/modification', association_views.modify_association, name='modify_association'),
    path('association/<int:asso_id>/ajout_membre', association_views.add_members, name='add_member'),
    path('association/invitation', association_views.invite_member, name='invite_member'),
    path('mes_associations/', association_views.my_association, name='my_association'),


    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^api/', include(api.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
