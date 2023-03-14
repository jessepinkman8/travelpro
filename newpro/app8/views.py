from django.shortcuts import render
from .models import info
from .models import team
# Create your views here.
def demo(request):
    obj=info.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'asd':obj1})