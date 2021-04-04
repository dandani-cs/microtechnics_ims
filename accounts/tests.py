from django.test import TestCase
from django.contrib.auth import get_user_model

from datetime import date
import random

def generate_id():
    return str(date.today().year) + str(random.randint(100000, 999999))

class UsersManagersTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username=generate_id(),
                                        email='normal@user.com',
                                        password='foo')

        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.username.startswith(str(date.today().year)))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(generate_id(),
                                                   'super@user.com',
                                                   'foo')

        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.username.startswith(str(date.today().year)))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
