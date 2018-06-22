from __future__ import unicode_literals
from django.utils.html import mark_safe
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField, PPOIField
def random_id():
    unique_id = get_random_string(
        length=18, allowed_chars='0123456789')
    return unique_id

def upload_image(instance, filename, *args, **kwargs):
    location = random_id()
    return "media/images/%s/%s" % (location, filename)


MENU_TYPES= (
    ('Wedding','Wedding'),
    ('Social Events','Social Events'),
    ('Sweet Sixteens','Sweet Sixteens'),
    ('Corporate','Corporate'),
)
# Create your models here.
class gallery_image(models.Model):
    my_order = models.PositiveIntegerField('Image Order',default=0, blank=False, null=False)
    image = VersatileImageField(upload_to=upload_image, null=True, blank=False, ppoi_field='ppoi')
    ppoi = PPOIField(
        'Image PPOI'
    )
    def __unicode__(self):
        return str(self.id)

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def returnCroppedImage(self):
        return self.image.crop['400x400'].url

    def image_tag(self):
        return mark_safe('<img src="%s" width=155/>' % (self.image.url))

class menu_entry(models.Model):
    menu_name = models.CharField(max_length=255, blank=False)
    menu_pdf = models.FileField(upload_to=upload_image, null=True, blank=False)
    my_order = models.PositiveIntegerField('Menu Order',default=0, blank=False, null=False)
    menu_type = models.CharField(
        blank=False,
        default='Weddings',
        choices=MENU_TYPES,
        max_length=120
    )

    
    def __unicode__(self):
        return self.menu_name


    class Meta(object):
        ordering = ['my_order']
        verbose_name = 'Menu Entry'
        verbose_name_plural = 'Menu Entries'


class news_entry(models.Model):
    content =  RichTextField()

    
    def __unicode__(self):
        return str(self.id)