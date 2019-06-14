from django.test import TestCase
from .models import Image,Category,Location 

# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.ian=Location(location="Nairobi");

    def test_instance(self):
        self.assertTrue(isinstance(self.ian,Location))

    
    def test_save_image(self):
        self.ian.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete(self):
        self.ian.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location)==0)