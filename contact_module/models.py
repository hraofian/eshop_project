from django.db import models

# Create your models here.
 
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300 , verbose_name='ایمیل') 
    full_name = models.CharField(max_length=300 , verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='پاسخ تماس با ما' , null=True , blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین' , default=False)

    
    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
    

 
class UserProfile(models.Model):
    name = models.CharField(max_length=300 , verbose_name='نام و نام خانوادگی')
    photo = models.ImageField(upload_to='images', verbose_name='عکس پروفایل')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'لیست پروفایل'

    def __str__(self):
        return self.name
    

class KarbaranTest(models.Model):
    name = models.CharField(max_length=300 , verbose_name='نام و نام خانوادگی')
    photo = models.ImageField(upload_to='images', verbose_name='عکس کاربر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'لیست کاربران'

    def __str__(self):
        return self.name
    





