from django.test import TestCase
from .models import photos,Category,Location
import datetime as dt

# Create your tests here.

#testing the photos class
class Testphotos(TestCase):
    # Set up method
    def setUp(self):
        self.category= Category(name = 'Travel')
        self.category.save()

        self.location