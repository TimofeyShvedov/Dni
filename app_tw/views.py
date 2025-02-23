from django.shortcuts import render
from django.views.generic import ListView

from app_tw.models import DescriptionModel


# Create your views here.
def risof(request):
    return render(request, "Dome.html")

class OtprListView(ListView):
    model = DescriptionModel
    template_name = "My.html"
    context_object_name = "Zapisi"