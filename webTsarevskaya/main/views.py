from django.shortcuts import render

def main(request):
    return render(request, 'main/main-page.html')

def clothes(request):
    return render(request, 'main/clothes-page.html')

def about(request):
    return render(request, 'main/about-page.html')

def form(request):
    return render(request, 'main/form-page.html')
