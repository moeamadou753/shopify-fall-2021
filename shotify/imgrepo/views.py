from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Image, ImageManager
from django.shortcuts import redirect

def index(request):
    img_list = Image.objects.order_by('-pub_date')
    template = loader.get_template('imgrepo/index.html')
    context = {'img_list': img_list}
    return HttpResponse(template.render(context,request))

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form':f})

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
    