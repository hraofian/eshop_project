from django.shortcuts import render, redirect
from django.urls import reverse

def contact_us_page(request):
    if request.method == "POST":
        print(request.POST["fullname"])
        return redirect(reverse('home_page'))
    return render(request, 'contact_module/contact_us_page.html',{})
    
