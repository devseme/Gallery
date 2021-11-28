from django.test import TestCase
from .models import photos,Category,Location
import datetime as dt

# Create your tests here.


# photos model tests
class photosTestCase(TestCase):

    def setUp(self):
        
        photos.objects.create(
            name="First Image",
            description="photos Description",
            location=Location.objects.create(position="photos Location"),
            category=Category.objects.create(name="photos Category"),
            image="https://res.cloudinary.com/mypicsgalore/image/upload/v1638107885/kkws4fbi2axt9lfaadxe.webp",
            date=None
        )

    def test_photos_name(self):
        """
        Test that the photos name is correct
        """
        image = photos.objects.get(name="First Image")
        self.assertEqual(image.name, "First Image")

    def test_photos_description(self):
        """
        Test that the image description is correct
        """
        image = photos.objects.get(name="First Image")
        self.assertEqual(image.description, "photos Description")

    def test_photos_location(self):
        """
        Test that the image location is correct
        """
        image = photos.objects.get(name="First Image")
        self.assertEqual(image.location.position, "photos Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = photos.objects.get(name="First Image")
        self.assertEqual(image.category.name, "photos Category")

    def test_image_image(self):
        """
        Test that the image image is correct
        """
        image = photos.objects.get(name="First Image")
        self.assertEqual(image.image, "https://res.cloudinary.com/mypicsgalore/image/upload/v1638107885/kkws4fbi2axt9lfaadxe.webp")


    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        image = photos.objects.get(name="First Image")
        self
#location tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(position="photos Location")

    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(position="photos Location")
        self.assertEqual(location.position, "photos Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(position="photos Location")
        self.assertEqual(str(location), "photos Location") 

# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="photos Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="photos Category")
        self.assertEqual(category.name, "photos Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="photos Category")
        self.assertEqual(str(category), "photos Category")        