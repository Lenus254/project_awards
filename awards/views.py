from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    # all_projects = Project.fetch_all_images()
    # return render(request,"index.html",{"all_images":all_projects})
    return render(request, 'index.html')
