from django.shortcuts import render
def home(request):
    return render(request, 'resume/home.html')

def about(request):
    return render(request, 'resume/about.html')

def contact(request):
    return render(request, 'resume/contact.html')
# Create your views here.
