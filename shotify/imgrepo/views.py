from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the Shotify Image Repository.")

def user_images(request, owner_id):
    response = "Here are all of the images belonging to user %s."
    return HttpResponse(response % owner_id)

def detail(request, username, image_id):
    response = "Here is the fingerprint of image %s."
    return HttpResponse(response % image_id)