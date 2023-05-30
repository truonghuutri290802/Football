from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#lưu trữ thông tin bóng đá
class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    matches = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:            
            url = self.image.url
        except:
            url = ""
        return url  

class Matches(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.home_team} v.s. {self.away_team}"