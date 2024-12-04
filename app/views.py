from django.shortcuts import render

# Create your views here.

def abc(request):
    d = {'a':30, 'b':40, 'name' : 'Abhinaba'}
    return render(request, 'abc.html', context = d)
