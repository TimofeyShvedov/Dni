import requests
import time
vse_streamers = ['XenoDBD','KnightLight']
for streamer in vse_streamers:


    url = f"https://twitchtracker.com/api/channels/summary/{streamer}"
    answer = requests.get(url=url)
    print(answer.json())
    time.sleep(3)