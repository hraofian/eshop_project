from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductTag(models.Model):
    tag = models.CharField(max_length=300 , verbose_name='تگ محصول')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural= 'تگ های محصولات'

    def __str__(self):
        return self.tag




class ProductCategory(models.Model):
    title = models.CharField(max_length=300 , verbose_name='عنوان')
    url_title = models.CharField(max_length=300 , verbose_name='عنوان در url')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ProductInformation(models.Model):
    color = models.CharField(max_length=200 , verbose_name='رنگ')
    size = models.CharField(max_length=200 , verbose_name='اندازه')

    def __str__(self):
        return f'({self.color} - {self.size} )'
    
    class Meta:
        verbose_name ='اطلاعات تکمیلی محصول '
        verbose_name_plural = 'اطلاعات تکمیلی محصولات'


class Product(models.Model):
    title = models.CharField(max_length=300)
    product_information = models.OneToOneField(
    ProductInformation, 
    on_delete=models.CASCADE, 
    related_name='product_information',
    null=True,
    blank=True)
    category = models.ForeignKey(ProductCategory 
    , on_delete=models.CASCADE , 
    null=True , 
    related_name='products',
    verbose_name='دسته بندی')
    product_tags = models.ManyToManyField(ProductTag)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)] , default=0)
    short_description = models.CharField(max_length=360 , null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="" , null=False , db_index=True , blank=True)

    def get_absolute_url(self):
        return reverse('product-detail' , args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} -  {self.price}"
    
    class Meta:
        verbose_name ='محصول '
        verbose_name_plural = 'محصولات  '


    