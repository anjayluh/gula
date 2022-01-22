from django.db import models
from django.conf import settings
from django.utils.html import mark_safe


CURRENCY = settings.CURRENCY


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    qty = models.PositiveIntegerField(default=0)
    image_path = models.ImageField(max_length=255,null=True,blank=True,upload_to='images/%Y/%m/%d')
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def image_path_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image_path))

    image_path_tag.short_description = 'Image'