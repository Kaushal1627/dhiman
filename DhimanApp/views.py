from django.shortcuts import redirect, render
from .  models import Contact

# Create your views here.
def index (request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        
        contact=Contact(name=name,email=email,subject=subject,msg=msg)
        contact.save()
        return redirect('/')
        
        
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')
def blog(request):
    return render(request,'blog_list.html')





