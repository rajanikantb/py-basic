from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'login/index.html')