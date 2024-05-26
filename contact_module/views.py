from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import ContactUs 
from django.views import View

# def contact_us_page(request):
#     if request.method == "POST":
#         print(request.POST["fullname"])
#         return redirect(reverse('home_page'))
#     return render(request, 'contact_module/contact_us_page.html',{})
    


class ContactUsView(View):
    def get(self,request):
        contact_form = ContactUsModelForm()   
        return render(request, 'contact_module/contact_us_page.html',{
            'contact_form': contact_form
        })

    def post(self,request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home_page')
        
        return render(request, 'contact_module/contact_us_page.html',{
            'contact_form': contact_form
            })








# def contact_us_page(request):
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)

#         if contact_form.is_valid():
#             # print(contact_form.cleaned_data)
#             # contact = ContactUs(
#             #     title=contact_form.cleaned_data.get('title'),
#             #     full_name=contact_form.cleaned_data.get('full_name'),
#             #     email=contact_form.cleaned_data.get('email'),
#             #     message=contact_form.cleaned_data.get('message'),
#             # )
#             # contact.save()
#             contact_form.save()

#             return redirect('home_page')
#     # contact_form = ContactUsForm()   
#     contact_form = ContactUsModelForm()   

#     return render(request, 'contact_module/contact_us_page.html',{
#         'contact_form': contact_form
#     })
    


    
