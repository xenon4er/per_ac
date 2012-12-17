"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from per_ac.users.models import *
from per_ac.accounts_department.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    def setUp(self):
        user = User.objects.create_user("test","test", "123")
        user.is_staf = True
        user.save()
        prof = UserProfile(user=user)
        prof.save()
        self.cat = Category.objects.create(Title = "first", periodicity = 10, FK_User =user )
        self.cat.save()
        per1 = Category.objects.filter(Title = "first")
        per = per1[0].periodicity
        self.assertEqual(per, 10)
    
