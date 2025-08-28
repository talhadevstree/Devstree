import requests
from dotenv import load_dotenv
import os

load_dotenv()
while True:
    print("Welcome to movie APP!!")
    choice = input("What you want to do ? \n 1. search movie\n 2. Get trending movie\n 3. upcoming movies\n 4. Find movie by ID\n 5. Search TV shows\n 6. Now playing movies\n 7. Trending TV shows \n" )
   
    token = os.getenv('bearer')
    headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
    
    if choice == '1':
        try:    
            movie = input("Enter movie name to find:")
            
            api = os.getenv("api")
            url = f"http://api.themoviedb.org/3/search/movie?api_key={api}&query={movie}"
            
            data = requests.get(url)
            res = data.json()
            print("Movie name:",res['results'][0]['title'])
            print("Release Date:",res['results'][0]['release_date'])
            print("overview:",res['results'][0]['overview'])
            

        except requests.exceptions.ConnectionError as e:
            print("connection error:",e)
        
    elif choice == "2":
        url = "https://api.themoviedb.org/3/movie/popular"
        token
        headers

        try:
            response = requests.get(url, headers=headers)
            data = response.json()

            if "results" in data:
                print("Popular Movies:\n")
                for movie in data["results"][:10]:  # show top 10 movies
                    print(f"Title: {movie['title']}")
                    print(f"Release Date: {movie['release_date']}")
                    print(f"Rating: {movie['vote_average']}")
                    print("-" * 40)
            else:
                print("No results found:", data)

        except requests.exceptions.ConnectionError as e:
            print("Connection error:", e)
            
    elif choice == '3':
        try:
            url = f"http://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

            token 
            headers

            response = requests.get(url, headers=headers)
            data = response.json()
            print(data['results'][0]['title'])
        except requests.exceptions.ConnectionError as e:
            print("connection error:", e)
    elif choice == '4':
       try:
           external_id = "12"  
        
           url = f"https://api.themoviedb.org/3/find/external_id?external_source={external_id}"

           token
           headers

           response = requests.get(url, headers=headers)
           data = response.json()
           print(data)
       except requests.exceptions.ConnectionError as e:
           print("connection error:",e)  
        
    elif choice == '5':
        try:
            tv = input("Enter TV show name: ")
            api = os.getenv("API")
            url = f"http://api.themoviedb.org/3/search/tv?api_key={api}&query={tv}"

            response = requests.get(url)
            data = response.json()

            if data['results']:
                print("TV Show Name:", data['results'][0]['name'])
                print("First Air Date:", data['results'][0]['first_air_date'])
                print("Overview:", data['results'][0]['overview'])
            else:
                print("No TV shows found.")

        except requests.exceptions.ConnectionError as e:
            print("Connection error:", e)
            
    elif choice =='6':
        try:
            api = os.getenv("api")
            token = os.getenv("bearer")
            url = f"http://api.themoviedb.org/3/movie/now_playing?api_key={api}&language=en-US&page=1"
            headers = {
                       "accept": "application/json",
                        "Authorization": f"Bearer {token}"
                      }
            response = requests.get(url , headers=headers)
            data = response.json()
            
            print("Movie Name:",data['results'][0]['title'])
                # print("Release Date:", data['results'][0]['release_date'])
        except requests.exceptions.ConnectionError as e:
            print("connection error" ,e )
    
    elif choice == '7':
        try:
            api = os.getenv('api')
            token = os.getenv('bearer')
            url = f"http://api.themoviedb.org/3/trending/tv/day?language=en-US"
            headers = {
                        "accept": "application/json",
                        "Authorization": f"Bearer {token}"
                    }
            
            response = requests.get(url , headers=headers)
            print(response['results']['name'])
        except requests.exceptions.ConnectionError as e:
            print("Connection error:" , e)
    else:
        print("Invalid operator")
        