from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'To do list.html')
def edit(request):
    return render(request, 'Edit-Page.html')