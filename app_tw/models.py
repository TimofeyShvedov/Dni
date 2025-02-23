from django.db import models

class DescriptionModel(models.Model):
    username = models.CharField(max_length=18)
    unique = models.CharField(max_length=500)
    mainer = models.CharField(max_length=500)
    gameplay = models.CharField(max_length=500)
    comp = models.CharField(max_length=500,null=True)
    team_dbd = models.CharField(max_length=500,null=True)
    url_tw = models.CharField(max_length=500)
    followers = models.IntegerField()
    photo = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
