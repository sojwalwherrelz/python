import requests
import json

apikey = "%APIKEY%"
id = "1f16f05e-e25c-43a1-ba00-331b1d2c3b8a"
response = requests.get("https://api.cricapi.com/v1/cricScore?apikey="+apikey+"&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    players = json.loads(text)['data']['players']
    print("----------------------------Fantacy Squad Score -----------------")
    if(data):
     for val in data:
      print(" teamName - "+val['teamName'])    
     for player in players:
      print(" name - "+val['name'] +" battingStyle - "+ str(val['battingStyle'])+"\n " +"role - "+ str(val['role']) )    
    
myobj(response.json())
