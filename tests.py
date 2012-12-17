"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from per_ac.views import GetMySavings
from per_ac.accounts_department.models import *
import datetime

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def test_GetMySavings(TestCase):
        user = User.objects.create_user("test2","test2", "123")
        user.is_staf = True
        user.save()
        prof = UserProfile(user=user)
        prof.save()
        
        self.safe = Safe.objects.create(Title = "test_safe",  FK_User = user)
        self.safe.save()
        #safe_test = Safe.objects.filter(Title = "first")
        
        self.cat = Category.objects.create(Title = "first", periodicity = 10, FK_User =user )
        self.cat.save()
        #cat_test = Category.objects.filter(Title = "first")
        date_test = datetime.date.today() 
        self.pay = Payments.objects.create(curency = "test", Reason = "test", FK_User =user, FK_Category = self.cat, Fk_Safe = self.safe,  Amount_of_payment =  10 , date = date_test )
        self.pay.save()
        
        self.assertEqual(GetMySavings(user), 10)
