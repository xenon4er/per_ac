from django.test import TestCase
from per_ac.accounts_department.models import *

class CategoryTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("test","test", "123")
        user.is_staf = True
        user.save()
        prof = UserProfile(user=user)
        prof.save()
        self.cat = Categoty.objects.create(Title = "first", periodicity = "sd", FK_User =user )
        self.assertEqual(self.cat.objects.filter(Title = "first").periodicity, 10000)
