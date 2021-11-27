from django.db import models
from cloudinary.models import CloudinaryField

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =50)

    @classmethod
    def search_by_name(cls,search_term):
        media = cls.objects.filter(name__icontains=search_term)
        return media
    