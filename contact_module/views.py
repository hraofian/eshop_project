from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import ContactUs 
from django.views.generic.edit import FormView, CreateView 
from django.views.generic import ListView
from django.views import View
from .models import *



class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/' 

  
def store_file(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            # print('chunk =', chunk)
            dest.write(chunk)





class CreatProfileView(View):
    def get(self, request):
        return render (request , 'contact_module/create_profile_page.html')
    
    def post(self, request):
        store_file(request.FILES['profile'])
        # return render(request, 'contact_module/create_profile_page.html')
        print('request = ',request.FILES)
        return redirect('/contact-us/create-profile/')


class UserProfileView(CreateView):
    template_name = 'contact_module/user_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/profile/'
    


class KarbaranVoroodView(CreateView):
    template_name = 'contact_module/karbaran_vorood.html'
    model = KarbaranTest
    fields = '__all__'
    success_url = '/contact-us/karbaran-vorood/'
    




class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'contact_module/user_profile_list.html'
    context_object_name = 'profiles'


class KarbaranTestView(ListView):
    model = KarbaranTest
    template_name = 'contact_module/karbaran.html'
    context_object_name = 'karbaran'
 


# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ContactUsView(View):
#     def get(self,request):
#         contact_form = ContactUsModelForm()   
#         return render(request, 'contact_module/contact_us_page.html',{
#             'contact_form': contact_form
#         })

#     def post(self,request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
        
#         return render(request, 'contact_module/contact_us_page.html',{
#             'contact_form': contact_form
#             })


# def contact_us_page(request):
#     if request.method == "POST":
#         print(request.POST["fullname"])
#         return redirect(reverse('home_page'))
#     return render(request, 'contact_module/contact_us_page.html',{})
    







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
    


    
