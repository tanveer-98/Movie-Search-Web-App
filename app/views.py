from django.shortcuts import render
import requests,json

def get_movie_details(moviename):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":moviename,"r":"json"}

    headers = {
        'x-rapidapi-key': "abd90c9bd4msha73c3c8faf90992p1528e2jsn3fb0fb4c129f",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    id = response.json()['Search'][1]['imdbID']
    # print('Total Fetched: {}'.format(len(response.json()['Search'])))
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"i":id,"r":"json"}
    headers = {
        'x-rapidapi-key': "abd90c9bd4msha73c3c8faf90992p1528e2jsn3fb0fb4c129f",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

# Create your views here.
def index(request):
    if(request.method =='POST'):
        data = request.POST
        moviename = data.get('Movie_Name')
        moviedetail = get_movie_details(moviename)
        rating = moviedetail['imdbRating']
        genre = moviedetail['Genre']
        Plot = moviedetail['Plot']
        metascore = moviedetail['Metascore']
        releasedate = moviedetail['Released']

        context = {'moviename':moviename,'rating':rating,'genre':genre,'Plot':Plot,
        'metascore': metascore, 'releasedate':releasedate,'Plot':Plot}
        return render(request,'details.html',context)
    return render(request,'index.html')

def details(request):
    return render(request,'details.html')
