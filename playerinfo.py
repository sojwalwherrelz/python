import requests
import json

apikey = "%APIKEY%"
id="af71b5ba-97e0-4dd6-9914-832ed1bf62c5"
response = requests.get("https://api.cricapi.com/v1/players_info?apikey="+apikey+"&offset=0&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    print("----------------------------Players Info -----------------")
    print(" Name - "+data['name']+" \n "+"date Of Birth -   "+data['dateOfBirth']+" \n ")    
    print(" batting Style - "+data['battingStyle'] +" bowling Style - "+ str(data['bowlingStyle']) +" place Of Birth - "+ str(data['placeOfBirth']) )    
    print(" country - "+data['country'] +" player Img - "+ str(data['playerImg']) )    

myobj(response.json())
