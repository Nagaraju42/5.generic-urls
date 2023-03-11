from django.shortcuts import render

# Create your views here.
def template1(request):
    return render(request,'template1.html')