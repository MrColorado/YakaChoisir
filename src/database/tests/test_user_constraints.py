from django.contrib.auth.models import User
from django.test import TestCase
from django.db.utils import IntegrityError

from database.models import Association, Members, myUser


class ConstraintTests(TestCase):

    def test_unique_user(self):
        """Checking that Users are unique"""
        user_ok = User.objects.create_user(username='test')
        user_ok.save()
        with self.assertRaises(IntegrityError) as context:
            user_fail = User.objects.create_user(username='test')
            user_fail.save()

    def test_unique_association_members(self):
        user = User.objects.create_user(username='test')
        asso = Association(name='Testings')

        user.save()
        asso.save()

        member_ok = Members(user_id=myUser.objects.get(user=user), association_id=asso)
        member_fail = Members(user_id=myUser.objects.get(user=user), association_id=asso)

        member_ok.save()
        with self.assertRaises(IntegrityError) as context:
            member_fail.save()
