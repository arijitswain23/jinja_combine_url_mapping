from django.shortcuts import render

# Create your views here.
def sp_iterator(request):
    return render(request,'sp_iterator.html')

def sp_generator(request):
    return render(request,'sp_generator.html')