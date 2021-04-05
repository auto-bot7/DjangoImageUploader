from django.shortcuts import render
from .models import Image 
from .forms import ImageForm
# Create your views here.
def home(request):
    if request.method=="POST":
        form = ImageForm(request.POST, request.FILES) # if req is POST or if an image is uploaded, include request.FILES & enctype=multipart/form-data(in form field in html file) while working with images
        if form.is_valid(): #check if it is valid
            form.save()          #save 
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'api/home.html',{'img':img, 'form':form})  #include this reference form in home.html