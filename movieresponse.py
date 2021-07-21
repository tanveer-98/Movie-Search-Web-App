import requests,json

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"s":"Cars","r":"json"}

headers = {
    'x-rapidapi-key': "abd90c9bd4msha73c3c8faf90992p1528e2jsn3fb0fb4c129f",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
id = response.json()['Search'][1]['imdbID']
print(id)
print('***** RESPONSE *****')
print(response.json())

print('***** RESPONSE *****')

print('Total Fetched: {}'.format(len(response.json()['Search'])))
url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"i":id,"r":"json"}

headers = {
    'x-rapidapi-key': "abd90c9bd4msha73c3c8faf90992p1528e2jsn3fb0fb4c129f",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }


response = requests.request("GET", url, headers=headers, params=querystring)



print(response.json()['imdbRating'])
print(response.json())
