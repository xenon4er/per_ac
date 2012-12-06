from django.test import TestCase
from per_ac.accounts_department.models import *
from django.contrib.auth.models import User
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        u = User(1, "adadasd", "dadad")
        #u = self.us.objects.filter(email = "dsdd")
        self.cat = Category.objects.create(Title = "first",  periodicity =2,  FK_User = u)
        self.assertEqual(self.cat.objects.filter(Title = "first").periodicity, 3)
