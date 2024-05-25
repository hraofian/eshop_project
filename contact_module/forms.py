from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):   

    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_lenght': 'نام و نام خانوادگی نمی تواند بیش از 50 کاراکتر داشته باشد',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی',
        })
        )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': ' ایمیل  ',  
        })
        )
    title = forms.CharField(
        label='عنوان',
         widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' عنوان  ',  
        })
        )
    message = forms.CharField(
        label='متن پیام' , 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': ' متن پیام  ', 
            'id': 'message'
        })

        )
    



class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email' , 'title' , 'message']
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'rows': 5,
                'id':'message'
            }),
        }
        labels = {
            'full_name':'نام و نام خانوادگی شما',
            'email':'ایمیل شما',
            'title':'عنوان پیام شما',
            'message':'متن پیام شما',        

        }
        error_messages={
            'full_name':{
                'required': 'نام و نام خانوادگی اجباری می باشد'
            }
        }


 






