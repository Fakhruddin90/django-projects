from django.shortcuts import render
from django.http import HttpResponse

from .models import Personal

# Create your views here.
def index(request):
    # return HttpResponse("Hello world")
    context = {
        "personal": Personal.objects.all()
    }
    return render(request, 'personal/index.html', context)