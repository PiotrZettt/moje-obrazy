from django.shortcuts import render
from .models import Painting

# Create your views here.
def home(request):

    paintings = Painting.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, 'index.html', context)
