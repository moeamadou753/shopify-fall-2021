from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Image, ImageManager

def index(request):
    img_list = Image.objects.order_by('-pub_date')
    template = loader.get_template('imgrepo/index.html')
    context = {'img_list': img_list}
    return HttpResponse(template.render(context,request))

def user_images(request, owner_id):
    response = "Here are all of the images belonging to user %s."
    return HttpResponse(response % owner_id)

def detail(request, username, image_id):
    try:
        # Will throw an Image.DoesNotExist error if not found
        img = Image.objects.get(pk=image_id) 

        if img.image_owner == username:
            response = f"Here is the fingerprint of image {image_id}."  
        else:
            response = f"User {username} does not have permission to view image {image_id}."
    except Image.DoesNotExist:
        raise Http404(f"Image {image_id} does not exist.")

    return render(request, "imgrepo/detail.html", {'img' : img})
    