from django.test import TestCase
from per_ac.accounts_department.models import *

class CategoryTest(TestCase):
    def setUp(self):
        u = User()
        self.cat = Categoty.objects.create(Title = "first", periodicity = "sd", FK_User =u )
        self.assertEqual(self.cat.objects.filter(Title = "first").periodicity, 3)
