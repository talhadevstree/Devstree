import requests
import time


url = "https://randomuser.me/api/"
try:
    data = requests.get(url)
    data.raise_for_status()
    print(data)
except requests.exceptions.RequestException as error:
    print("Error while fetching data")
    
url = "github.com" 
try:
    data = requests.get(url)
    data.raise_for_status()
    print(data)
except requests.exceptions.MissingSchema as sch:
    print("Missing HTTPS Requests")



url= "https://github.com/"
for trial in range(3):
    try:
        data = requests.get(url , timeout=5)
        data.raise_for_status()
        response = data.json()
        print(response['results'][0]['name']['first'])
        break
    except requests.exceptions.RequestException as error:
        print(f"Attemt : {trial+1} failed:" ,error)
        time.sleep(2)
else:
    print("Failed to fetch data  after 3 attempt")
        
