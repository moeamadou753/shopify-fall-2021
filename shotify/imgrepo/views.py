from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Image, ImageManager
from .forms import UploadImageForm

from django.shortcuts import redirect

@login_required(login_url="/accounts/login/")
def index(request):
    img_list = Image.objects.order_by('-pub_date')
    template = loader.get_template('imgrepo/index.html')
    

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect('index')
    else:
        form = UploadImageForm()

    context = {'img_list': img_list, 'form': form}

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