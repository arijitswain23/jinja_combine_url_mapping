from django.shortcuts import render

# Create your views here.
def gn_overriding(request):
    return render(request,'gn_overriding.html')

def gn_overloading(request):
    return render(request, 'gn_overloading.html')