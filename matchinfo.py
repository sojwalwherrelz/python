import requests
import json

apikey = "%APIKEY%"
id="1f16f05e-e25c-43a1-ba00-331b1d2c3b8a"
response = requests.get("https://api.cricapi.com/v1/match_info?apikey="+apikey+"&offset=0&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    teams = json.loads(text)['data']['teams']
    print("----------------------------Match Info -----------------")
    print(" Name - "+data['name']+" \n "+"Match Type -   "+data['matchType']+" \n ")    
    print(" status - "+data['status'] +" venue - "+ str(data['venue']) +" date - "+ str(data['date']) )    
    for tm in teams:
     print(" tm - "+tm )    

myobj(response.json())
