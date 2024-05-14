from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class ProductCategory(models.Model):
    title = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده')

    def __str__(self):
        return f'({self.title} - {self.url_title})'
    
    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name=' دسته بندی ها')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360 , null=True , verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی')
    slug = models.SlugField(default="" , null=False , db_index=True , blank=True, unique=True)
    is_active = models.BooleanField(default=False , verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده/ نشده')

    def get_absolute_url(self):
        return reverse('product-detail' , args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name ='محصول '
        verbose_name_plural = 'محصولات  '

class ProductTag(models.Model):
    caption = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_tags')
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural= 'تگ های محصولات'

    def __str__(self):
        return self.caption

