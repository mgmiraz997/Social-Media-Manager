from django.shortcuts import render

def home(request):
    return render(request, "overview.html")
def overview(request):
    return render(request, "overview.html")

