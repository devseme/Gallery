from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import photos #import photos model
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    photo = photos.objects.all()
    
    return render(request, 'all-pics/index.html',{'photo':photo})  
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