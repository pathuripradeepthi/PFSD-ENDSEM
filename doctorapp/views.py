from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request, 'doctorapp/Homepage.html')

def Success(request):
    return render(request, 'doctorapp/Success.html')


