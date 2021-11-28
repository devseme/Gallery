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
     
    #image field
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def save_photos(self):
        self.save()


    # update photos
    def update_photos(self, name, description,category,location):
        self.name = name
        self.description = description
        self.category = category
        self.location =location
        self.save()
    # delete image from database
    def delete_image(self):
        self.delete()
    
    def _str_(self):
        return self.name
    
    @classmethod
    def filter_by_category(cls,search_term):
        images = cls.objects.filter(category_name_icontains=search_term)
        return images
    # get all photos
    @classmethod
    def get_image_by_id(cls, id):
        image = photos.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__name__icontains=search_term)
        return pics
    @classmethod
    def filter_by_location(cls,search_location):
        images = cls.objects.filter(location_name_icontains=search_location).all()
        return images    
    @classmethod
    def search(cls, search_term):
        images_by_category = cls.filter_by_category(search_term)
        images_by_location = cls.filter_by_location(search_term)
        return images_by_category.union(images_by_location)    
    
        
    