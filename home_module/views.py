from django.shortcuts import render

# Create your views here.
def index_pade(request):
    return render(request , 'home_module/index_page.html')