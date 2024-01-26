from django.shortcuts import render

def home(request):
    return render(request, 'photogallery/home.html')

def course(request):
    return render(request, 'photogallery/cource.html')

def gallery(request):
    return render(request, 'photogallery/gallery.html')

def contact(request):
    return render(request, 'photogallery/contact.html')

def about(request):
    return render(request, 'photogallery/about.html')