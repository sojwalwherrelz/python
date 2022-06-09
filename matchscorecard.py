import requests
import json

apikey = "%APIKEY%"
id="1f16f05e-e25c-43a1-ba00-331b1d2c3b8a"
response = requests.get("https://api.cricapi.com/v1/match_scorecard?apikey="+apikey+"&offset=0&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    teamInfo = json.loads(text)['data']['teamInfo']
    print("----------------------------Matchscore Card -----------------")
    print(" Name - "+data['name']+" \n "+"match Type -   "+data['matchType']+" \n ")    
    print(" status - "+data['status'] +" date - "+ str(data['date'])+"\n " +"venue - "+ str(data['venue']) )    
    print("----------------------------Team Info -----------------")
    for teamInfos in teamInfo:
        print(teamInfos['name'])
        print(teamInfos['shortname'])
        print(teamInfos['img'])
myobj(response.json())
