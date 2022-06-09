import requests
import json

apikey = "%APIKEY%"
searchName = "Dhananjaya kshan"
playerName = searchName.replace(" ", "%20")
response = requests.get("https://api.cricapi.com/v1/players?apikey="+apikey+"&offset=0&search"+playerName)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    # print(data)
    print("----------------------------Player Search List -----------------")
    for value in data:
        print("Name - "+value['name']+"  Country Name -   "+value['country'])    

myobj(response.json())
