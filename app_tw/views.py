from django.shortcuts import render
from django.views.generic import ListView
import requests
import time
from app_tw.models import DescriptionModel


# Create your views here.
def risof(request):
    vse_streamers = DescriptionModel.objects.all().values_list("username",flat=True)
    for streamer in vse_streamers:
        url = f"https://twitchtracker.com/api/channels/summary/{streamer}"
        answer = requests.get(url=url)
        try:

            subcribes=answer.json()["followers_total"]
        except Exception:
            continue
        DescriptionModel.objects.filter(username=streamer).update(followers=subcribes)
        time.sleep(3)
    return render(request, "Dome.html")

class OtprListView(ListView):
    model = DescriptionModel
    template_name = "My.html"
    context_object_name = "Zapisi"
