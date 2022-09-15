from django.db import models
from apps.common.models import TimeStampedModel
# Create your models here.



class Category(TimeStampedModel): 
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)
class Product(TimeStampedModel):
    # title = models.CharField(max_length=255) 
    # description = models.CharField(max_length=255)
    # price  = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True,null=True)
    pic = models.ImageField(upload_to='media/',null=True,blank=True)
    pic1 = models.ImageField(upload_to='media/',null=True,blank=True)
    pic2 = models.ImageField(upload_to='media/',null=True,blank=True)
    discount_price = models.FloatField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    category = models.ManyToManyField(Category, related_name="products")
    label = models.CharField(choices=LABEL_CHOICES,max_length=10,blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    # def get
