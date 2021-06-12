from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
data = {'summer':1, 'men':2}
class Category(models.Model):

    name = models.CharField( max_length=255)
    slug = models.SlugField(max_length = 255, unique = True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=False)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ("-name", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'



class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
    image = models.ImageField(upload_to='uploads/', blank =True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank = True, null= True)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255,help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE ,null= True) 


    class Meta:
        ordering: ("-created_at")


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # if self.categories.slug in data:
        #     data_slug = data[self.categories.slug]
        # else:
        #     data_slug =None

        return f'/{self.categories.id}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url 
        return None

    def get_thumbnail_image(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' +   self.thumbnail.url 
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image) 
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url 
            else :
                return None

    def make_thumbnail(self,image ,size=(300,200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG', quality=85)

        thumbnail = File(thumb_io,name=image.name)

        return thumbnail

