import uuid
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.utils import timezone

from api_product.models import Category


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.CharField(max_length=300, null=True, blank=True)
    thumbnail = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated_at',)
        db_table = 'product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return "https://res.cloudinary.com/dsa93ocf0/" + self.image
        return ""

    def get_thumbnail(self):
        # if self.thumbnail:
        #     return self.thumbnail.url
        # else:
        #     if self.image:
        #         self.thumbnail = self.make_thumbnail(self.image)
        #         self.save()
        #
        #         return self.thumbnail
        #     else:
        return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail