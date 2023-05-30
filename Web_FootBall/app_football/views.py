from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import *
# Create your views here.
def home(response):
    return render(response, 'app/home.html')
def premierleague(request):
    # Truy xuất tất cả các đội bóng thuộc về giải Premier League
    premier_league_teams = Team.objects.filter(league__name='Premier League').order_by('-points')

    # Truy xuất thông tin về giải đấu Premier League
    premier_league = League.objects.get(name='Premier League')
    
    # Truy xuất thông tin các trận đấu
    matches =Matches.objects.filter(league__name='Premier League')

    context = {
        'league': premier_league,
        'teams': premier_league_teams,
        'matches': matches
    }
    # Truyền dữ liệu vào template và hiển thị bảng xếp hạng,các trận đấu
    return render(request, 'app/premierleague.html', context)

def laliga(request):
    # Truy xuất tất cả các đội bóng thuộc về giải Premier League
    laliga_teams = Team.objects.filter(league__name='LaLiGa').order_by('-points')

    # Truy xuất thông tin về giải đấu Premier League
    laliga = League.objects.get(name='LaLiGa')
    
    matches =Matches.objects.filter(league__name='LaLiGa')
    # Truyền dữ liệu vào template và hiển thị bảng xếp hạng
    return render(request, 'app/laliga.html', {'league': laliga, 'teams': laliga_teams,'matches':matches}) 

def bundesliga(request):
    # Truy xuất tất cả các đội bóng thuộc về giải Premier League
    bundesliga_teams = Team.objects.filter(league__name='Bundesliga').order_by('-points')

    # Truy xuất thông tin về giải đấu Premier League
    bundesliga = League.objects.get(name='Bundesliga')
    
    matches =Matches.objects.filter(league__name='Bundesliga')
    
    context = {
        'teams': bundesliga_teams,
        'league': bundesliga,
        'matches': matches
    }
    # Truyền dữ liệu vào template và hiển thị bảng xếp hạng
    return render(request, 'app/bundesliga.html', context)