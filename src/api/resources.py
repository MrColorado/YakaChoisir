from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from tastypie import fields
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie.constants import ALL
from tastypie.resources import Resource, ModelResource

from database.models import Attend, Members, Event, myUser


class MembersResource(ModelResource):
    class Meta:
        queryset = Members.objects.all()
        resource_name = 'members'
        authorization = ReadOnlyAuthorization()


class EventsResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization = ReadOnlyAuthorization()


class UsersResource(ModelResource):
    class Meta:
        queryset = myUser.objects.all()
        resource_name = 'users'
        authorization = ReadOnlyAuthorization()


class EventMembersResource(ModelResource):
    class Meta:
        queryset = Attend.objects.all()
        resource_name = 'event_members'
        authorization = ReadOnlyAuthorization()

    def dehydrate(self, bundle):
        """Add extra fields to our request result."""
        bundle.data['token'] = bundle.obj.event_id.token_staff
        bundle.data['firstname'] = bundle.obj.user_id.user.first_name
        bundle.data['lastname'] = bundle.obj.user_id.user.last_name
        bundle.data['email'] = bundle.obj.user_id.user.email
        return bundle
