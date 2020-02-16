def get_genre(movie):
    import tmdbsimple as tmdb
    tmdb.API_KEY = 'API_KEY'
    search = tmdb.Search()
    response = search.movie(query=movie)
    try:
        movie = tmdb.Movies(int(search.results[0]['id']))
    except:
        return
    response = movie.info()

    list=[]
    for item in movie.genres:
        list.append(item['name'])
    return list

def get_id(movie):
    import tmdbsimple as tmdb
    tmdb.API_KEY = 'API_KEY'
    search = tmdb.Search()
    response = search.movie(query=movie)
    movie = tmdb.Movies(int(search.results[0]['id']))
    return movie

def get_similar(movie):
        import tmdbsimple as tmdb
        tmdb.API_KEY = 'API_KEY'
        search = tmdb.Search()
        id = get_id(movie)
        similar = id.similar_movies()['results']
        list=[]
        for item in similar:
            list.append({"Title": item['title'],
                        "Release_Date": item['release_date'],
                        "Desc": item['overview'],
                        "Genre": ', '.join(get_genre(item['title'])),
                        "Rating": item['vote_average'],
                        "Image": get_images(item['title'])})
        return list

def get_images(movie):
    import tmdbsimple as tmdb
    tmdb.API_KEY = 'API_KEY'
    search = tmdb.Search()
    response = search.movie(query=movie)
    return ("http://image.tmdb.org/t/p/w185/" + search.results[0]['poster_path'])

def new_movies(emotions):

    joy = emotions['joy']
    surprise = emotions['surprise']
    sorrow = emotions['sorrow']
    anger = emotions['anger']

    import heapq
    temp=[joy,surprise,sorrow,anger]
    temp = heapq.nlargest(2,temp)
    joyb = False
    surp = False
    sorp = False
    angp = False
    if joy in temp:
        joyb=True
    if surprise in temp:
        surp = True
    if sorrow in temp:
        sorp = True
    if anger in temp:
        angp = True

    if joyb and angp:
        return get_similar("Knives Out")
    elif joyb and surp:
        return get_similar("Zombieland")
    elif joyb and sorp:
        return get_similar("Captain Philips")
    elif surp and sorp:
        return get_similar("Titanic")
    elif surp and angp:
        return get_similar("The Matrix Reloaded")
    elif sorp and angp:
        return get_similar("Parasite")

