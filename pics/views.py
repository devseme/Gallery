from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import photos,Category,Location 
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    photo = photos.objects.all().order_by('-id')
    
    
    # if 'category' in request.GET and request.GET["category"]:
    #     category_id = request.GET.get("category")
    #     photo = photos.objects.filter(category = category_id)
        
    # elif 'location' in request.GET and request.GET["location"]:
    #     location_id = request.GET.get("location")
    #     photo = photos.objects.filter(location = location_id)
       
    # else:
    #     photo = photos.objects.all()
            
    # ctx = {'photos':photo, 'categories': categories, 'locations':locations }
    return render(request, 'all-pics/index.html',{'locations':locations,'photo':photo})
    
def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_images = photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photos": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

# def image(request,image_id):
#     try:
#         Image = photos.objects.get(id = image_id)
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,"all-pics/image.html", {"image":image})