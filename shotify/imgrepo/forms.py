from django.forms import ModelForm
from .models import Image

class UploadImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_owner', 'image_slug', 'image_permissions', 'image_src']
