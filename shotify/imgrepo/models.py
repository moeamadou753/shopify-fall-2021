from django.db import models

class ImageManager(models.Manager):
    def create_image(self, owner, slug, permissions, src, pub_date):
        image = self.create(owner=owner, slug=slug, permissions=permissions, src=src, pub_date=pub_date)
        # do something with the image
        return image

class Image(models.Model):
    image_owner = models.CharField(max_length=30)
    image_slug = models.SlugField(max_length=200)
    image_permissions = models.CharField(max_length=1, choices=[('+', 'PUBLIC'), ('-', 'PRIVATE')], default='+')
    image_src = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    objects = ImageManager()

    def __str__(self):
        return f"{self.image_slug} by {self.image_owner} on {self.pub_date}"
