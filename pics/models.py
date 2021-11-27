from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    position = models.CharField(max_length =30)
    

    def __str__(self):
        return self.position
class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)

    def save_photos(self):
        self.save()


    # update photos
    def update_photos(self, name, description,category,location):
        self.name = name
        self.description = description
        self.category = category
        self.location =location
        self.save()

    # get all photos
    @classmethod
    def get_all_photos(cls):
        images = photos.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__name__icontains=search_term)
        return pics

        
    