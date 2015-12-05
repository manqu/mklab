from django.db import models
from django.db.models.signals import pre_save
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from shop.utils import random_name_upload_to, thumbnail

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.message

class Item(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True)
    name = models.CharField(max_length=100)
    main_image = models.ImageField(blank=True, null=True, upload_to= random_name_upload_to)
    description = models.ImageField(blank=True, null=True, upload_to= random_name_upload_to)
    content = models.TextField()
    price = models.IntegerField()
    stock = models.BooleanField()
    comments = GenericRelation(Comment)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Item, related_name='item_image', blank=True, null=True)
    item_image = models.ImageField(blank=True, null=True, upload_to=random_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Featured(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=150)
    content = models.TextField()
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class FeaturedMainImage(models.Model):
    featured = models.ForeignKey(Featured, related_name='image', blank=True, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= random_name_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
