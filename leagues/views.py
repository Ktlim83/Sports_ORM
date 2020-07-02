from django.shortcuts import render, redirect
from django.db.models import Q
from .models import League, Team, Player

from . import team_maker

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")



def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		"players": Player.objects.all(),
		"players": Player.objects.filter(Q(first_name__contains='Alexander')|Q(first_name__contains='Wyatt'))
		

	}

	return render(request, "leagues/index.html", context)






# "leagues" : League.objects.filter(name__contains="Baseball")
# "leagues" : League.objects.filter(name__contains="Women")
# "leagues" : League.objects.filter(sport__contains="Hockey")
# "leagues" : League.objects.exclude(name__contains="football")
# "leagues" : League.objects.filter(name__contains="conference")
# "leagues" : League.objects.filter(name__contains="Atlantic")
# "teams" : Team.objects.filter(location__contains="Dallas")
# "teams" : Team.objects.filter(team_name__contains="Raptors")
# "teams" : Team.objects.filter(location__contains="City")
# "teams": Team.objects.filter(team_name__istartswith ='t')
# "teams" : Team.objects.order_by('location')
# "teams" : Team.objects.order_by('-location')
# "players" : Player.objects.filter(last_name__contains="Cooper")
# "players" : Player.objects.filter(first_name__contains="Joshua")
# "players" :Player.objects.filter(last_name__contains='Cooper').exclude(first_name__contains="Joshua")
# "players" : Player.objects.filter(first_name__contains='Alexander').filter(first_name__contains='Wyatt')

# from django.db.models import Q   <------neded to do OR
# "players": Player.objects.filter(Q(first_name__contains='Alexander')|Q(first_name__contains='Wyatt'))








# "leagues" : League.objects.filter(sport="Baseball"),


# ...all baseball leagues
# ...all womens' leagues
# ...all leagues where sport is any type of hockey
# ...all leagues where sport is something OTHER THAN football
# ...all leagues that call themselves "conferences"
# ...all leagues in the Atlantic region
# ...all teams based in Dallas
# ...all teams named the Raptors
# ...all teams whose location includes "City"
# ...all teams whose names begin with "T"
# ...all teams, ordered alphabetically by location
# ...all teams, ordered by team name in reverse alphabetical order
# ...every player with last name "Cooper"
# ...every player with first name "Joshua"
# ...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
# ...all players with first name "Alexander" OR first name "Wyatt"